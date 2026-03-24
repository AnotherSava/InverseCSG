import os, sys, subprocess
import readline, glob # For autocompleting file path.
import urllib.request
import shutil
import helper
import argparse

HERE = os.path.abspath(os.path.dirname(__file__))

# Logics behind this script: it tries to check if all necessary dependences are
# installed. If any of them is missing, it will attempt to download and install
# them, which may require adding new environment variables. To avoid polluting
# users' environment variables, we will save them into an ENVIRONMENT file and
# load them at the beginning of our scripts.

################################################################################
# Helpers.
################################################################################

# Credit:
# https://stackoverflow.com/questions/6656819/filepath-autocompletion-using-users-input
def AutoComplete(text, state):
  return (glob.glob(text + '*') + [None])[state]

def SaveCustomizedEnvironmentVariables(env_variables, file_path):
  with open(file_path, 'w') as f:
    f.write('# You can manually change the environment variables below:\n')
    for key, val in env_variables.items():
      f.write('%s: %s\n' % (key, val))

def CheckVersionNumber(version_number, target):
  major, minor, change = version_number.split('.')
  major = int(major)
  minor = int(minor)
  change = int(change)
  target_major, target_minor, target_change = target.split('.')
  target_major = int(target_major)
  target_minor = int(target_minor)
  target_change = int(target_change)
  if major > target_major:
    return True
  if major < target_major:
    return False
  if minor > target_minor:
    return True
  if minor < target_minor:
    return False
  if change >= target_change:
    return True
  else:
    return False
  
def CheckSketch(build_folder):
  sketch_result = subprocess.getoutput('sketch')
  # The first line should be something like:
  # SKETCH version 1.7.4
  # The following is not a very robust way to check the version number.
  if 'SKETCH version' not in sketch_result:
    return False
  # Now check version number.
  first_line = sketch_result.splitlines()[0]
  _, _, version_number = first_line.strip().split()
  # Expect to see >= 1.7.4.
  if not CheckVersionNumber(version_number, '1.7.4'):
    return False
  # Now Sketch seems working.
  helper.PrintWithGreenColor('Sketch %s seems successfully installed.' %
                       version_number)
  # Save environment variables into files.
  sketch_loc = subprocess.getoutput('whereis sketch')
  env_variables['CSG_SKETCH'] = sketch_loc.strip().split()[1].strip()
  # Auto-complete paths.
  readline.set_completer_delims(' \t\n;')
  readline.parse_and_bind('tab: complete')
  readline.set_completer(AutoComplete)

  # try local first : build/sketch/sketch-frontend
  sketch_frontend_folder = os.path.join(build_folder, 'sketch', 'sketch-frontend')
  if os.path.exists(sketch_frontend_folder):
    env_variables['CSG_SKETCH_FRONTEND'] = sketch_frontend_folder
  sketch_backend_folder = os.path.join(build_folder, 'sketch', 'sketch-backend')
  if os.path.exists(sketch_backend_folder):
    env_variables['CSG_SKETCH_BACKEND'] = sketch_backend_folder

  err_cnt = 0
  while 'CSG_SKETCH_FRONTEND' not in env_variables:
    sketch_frontend_folder = input('Tell us the location of sketch-frontend: ') 
    if not os.path.exists(sketch_frontend_folder):
      print('Folder does not exist. Please try again.')
      err_cnt += 1
      continue
    env_variables['CSG_SKETCH_FRONTEND'] = sketch_frontend_folder
    if err_cnt > 5:
      print('CSG_SKETCH_FRONTEND not found in environment variables. Re-download.')
      return False

  err_cnt = 0
  while 'CSG_SKETCH_BACKEND' not in env_variables:
    sketch_backend_folder = input('Tell us the location of sketch-backend: ') 
    if not os.path.exists(sketch_backend_folder):
      print('Folder does not exist. Please try again.')
      err_cnt += 1
      continue
    env_variables['CSG_SKETCH_BACKEND'] = sketch_backend_folder
    if err_cnt > 5:
      print('CSG_SKETCH_BACKEND not found in environment variables. Re-download.')
      return False

  return True

def InstallCGAL():
  helper.Run('sudo apt-get install -y libcgal-dev')
  helper.PrintWithGreenColor('Installed libcgal-dev (system package)')

def InstallEigen(root_folder):
  # Prefer system Eigen3. Fall back to downloading vendored copy.
  exit_code = helper.Run('dpkg -s libeigen3-dev', None)
  if exit_code == 0:
    helper.PrintWithGreenColor('Using system Eigen3 (libeigen3-dev)')
  else:
    helper.PrintWithGreenColor('System Eigen3 not found, downloading vendored copy...')
    cpp_lib_folder = os.path.join(root_folder, 'cpp', 'lib')
    zip_path = os.path.join(cpp_lib_folder, 'eigen-3.3.4.zip')
    helper.Run('wget -q -O %s https://gitlab.com/libeigen/eigen/-/archive/3.3.4/eigen-3.3.4.zip' % zip_path)
    helper.Run('unzip -o -q %s -d %s' % (zip_path, cpp_lib_folder))
    os.remove(zip_path)
    # Rename extracted directory to match expected name (GitLab archives
    # may include a commit hash suffix like eigen-3.3.4-<hash>).
    expected = os.path.join(cpp_lib_folder, 'eigen-3.3.4')
    if not os.path.isdir(expected):
      for name in os.listdir(cpp_lib_folder):
        if name.startswith('eigen-3.3.4'):
          os.rename(os.path.join(cpp_lib_folder, name), expected)
          break
    helper.PrintWithGreenColor('Installed vendored Eigen 3.3.4')

def InstallJava():
  helper.Run('sudo apt-get install -y default-jdk')

  # Currently JAVA_HOME is hard coded.
  # java_home = '/usr/lib/jvm/java-8-oracle/' 
  # java_home = '/usr/lib/jvm/java-8-openjdk-amd64'
  java_path_cmd = "jrunscript -e \'java.lang.System.out.println(java.lang.System.getProperty(\"java.home\"));\'"
  java_home, _ = helper.Run(java_path_cmd, return_msg=True)
  env_variables['JAVA_HOME'] = os.environ['JAVA_HOME'] = java_home
  path = os.path.join(java_home, 'bin') + ':' + os.environ['PATH']
  env_variables['PATH'] = os.environ['PATH'] = path
  # helper.Run('%s -version' % os.path.join(java_home, 'bin', 'javac'))
  helper.Run('%s -version' % os.path.join(java_home, 'bin', 'java'))

def InstallMaven():
  # maven_url = 'http://mirrors.koehn.com/apache/maven/maven-3/3.5.3/' \
  #             'binaries/apache-maven-3.5.3-bin.zip'
  # maven_file = os.path.join(build_folder, 'maven.zip')
  # urllib.request.urlretrieve(maven_url, maven_file)
  # helper.Run('unzip -q %s -d %s' % (maven_file, build_folder))
  # os.remove(maven_file)
  # Add it to the environment variable.
  # for folder_name in os.listdir(build_folder):
  #   if 'maven' in folder_name:
  #     maven_loc = os.path.join(build_folder, folder_name, 'bin')
  #     env_variables['PATH'] = os.environ['PATH'] \
  #                           = maven_loc + ':' + os.environ['PATH']
  helper.Run('sudo apt-get install -y maven')
  # Check maven.
  helper.Run('mvn -v')

################################################################################
# Variables.
################################################################################
env_variables = {}

################################################################################
# Beginning of the script.
################################################################################

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--build_dir', default='', help='build directory path.')
    parser.add_argument('-dp', '--deps', action='store_false', help='Disable apt-get & py3 dependencies.')
    parser.add_argument('-eg', '--eigen', action='store_false', help='Disable Eigen install.') 
    parser.add_argument('-cg', '--cgal', action='store_false', help='Disable CGAL install.')
    parser.add_argument('-c', '--cpp', action='store_false', help='Disable source cpp compilation.')
    parser.add_argument('-sk', '--sketch', action='store_false', help='Disable sketch installation.')
    args = parser.parse_args()
    print('Arguments:', args)

    # Usage: python3 install.py -d <build folder>
    if not args.build_dir:
      print('Usage: python3 install.py -d <build_folder>')
      sys.exit(-1)

    build_folder = os.path.realpath(args.build_dir)
    root_folder = HERE
    if not os.path.exists(build_folder):
      os.makedirs(build_folder)
    helper.PrintWithGreenColor('Build folder created :{}'.format(build_folder))
    
    # Add a new environment variable to save the location of the root folder.
    env_variables['CSG_ROOT'] = os.environ['CSG_ROOT'] = root_folder
    
    # Check all C++ dependencies.
    if args.deps:
      print('Installing build tools and dependencies...')
      helper.Run('sudo apt-get update')
      helper.Run('sudo apt-get install -y build-essential autoconf libtool '
        'flex bison cmake git')

      # Install python dependencies.
      os.environ['PIP_BREAK_SYSTEM_PACKAGES'] = '1'
      helper.Run('python3 -m pip install -U pip setuptools')
      helper.Run('python3 -m pip install numpy scipy matplotlib scikit-learn')
    
    # Install CGAL.
    if args.cgal:
      InstallCGAL()

    # Install Eigen-3.3.4.
    if args.eigen:
      InstallEigen(root_folder)
    
    # Compile cpp.
    cpp_build_folder = os.path.join(build_folder, 'cpp')
    if not os.path.exists(cpp_build_folder):
      os.makedirs(cpp_build_folder)
    if args.cpp:
      os.chdir(cpp_build_folder)
      helper.Run('cmake %s' % os.path.join(root_folder, 'cpp'))
      helper.Run('make')
      helper.PrintWithGreenColor('C++ program compiled successfully.')
    env_variables['CSG_CPP_EXE'] = os.path.join(cpp_build_folder,
                                                'csg_cpp_command')
    
    # Install Sketch.
    # Try calling Sketch. If it is successful, we are done.
    if CheckSketch(build_folder):
      SaveCustomizedEnvironmentVariables(env_variables, os.path.join(
        build_folder, 'ENVIRONMENT'))
      helper.PrintWithGreenColor('Installation Done.')
      sys.exit(0)
    
    # If we are here, Sketch is not properly installed.
    # First, install Java JDK.
    print('Attempt to install Java JDK. Asking for sudo privilege.')
    InstallJava()
    
    # Next, install maven.
    InstallMaven()
    
    # * Download sketch-backend.
    sketch_folder = os.path.join(build_folder, 'sketch')
    if not os.path.exists(sketch_folder):
      os.makedirs(sketch_folder)
    if args.sketch:
      # Sketch-backend.
      os.chdir(sketch_folder)
      # ! the bitbucket repos are deleted at the time of Sep/3/2020
      # helper.Run('hg clone https://bitbucket.org/gatoatigrado/sketch-backend')
      # helper.Run('mv sketch-backend sketch-backend-default')
      # helper.Run('mv sketch-backend sketch-backend-default')
      # Use this version of sketch.
      # helper.Run('hg clone -r 04b3403 sketch-backend-default sketch-backend')
      # https://people.csail.mit.edu/asolar/
      helper.Run('git clone https://github.com/asolarlez/sketch-backend.git')

    sketch_backend_folder = os.path.join(sketch_folder, 'sketch-backend')
    env_variables['CSG_SKETCH_BACKEND'] = sketch_backend_folder

    # * build sketch backend
    if args.sketch:
      os.chdir(sketch_backend_folder)
      helper.Run('bash autogen.sh')
      helper.Run('./configure')
      helper.Run('make -j2')
      # Interestingly, I need to manually do the following copy and paste work to
      # avoid an error in sketch-frontend.
      sketch_solver_folder = os.path.join(sketch_backend_folder, 'src/SketchSolver')
      shutil.copyfile(os.path.join(sketch_solver_folder, 'libcegis.a'), \
                      os.path.join(sketch_solver_folder, '.libs/libcegis.a'))
      shutil.copyfile(os.path.join(sketch_solver_folder, 'cegis'), \
                      os.path.join(sketch_solver_folder, '.libs/cegis'))
    
    # Download sketch-frontend.
    os.chdir(sketch_folder)
    if args.sketch:
      # helper.Run('hg clone https://bitbucket.org/gatoatigrado/sketch-frontend')
      # helper.Run('mv sketch-frontend sketch-frontend-default')
      # # Use this version of sketch.
      # helper.Run('hg clone -r 42c057c sketch-frontend-default sketch-frontend')
      helper.Run('git clone https://github.com/asolarlez/sketch-frontend.git')
    sketch_frontend_folder = os.path.join(sketch_folder, 'sketch-frontend')
    env_variables['CSG_SKETCH_FRONTEND'] = sketch_frontend_folder
    os.chdir(sketch_frontend_folder)
    if args.sketch:
      helper.Run('make system-install DESTDIR=/usr/bin SUDOINSTALL=1')
    
    # Now check Sketch again.
    if not CheckSketch(build_folder):
      helper.PrintWithRedColor('Failed to install Sketch. Please fix.')
      sys.exit(-1)
    
    SaveCustomizedEnvironmentVariables(env_variables, os.path.join(
      build_folder, 'ENVIRONMENT'))
    helper.PrintWithGreenColor('Installation Done.')


if __name__ == '__main__':
    main()
