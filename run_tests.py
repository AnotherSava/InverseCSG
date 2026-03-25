import os
import shlex
import sys

# Usage: python3 run_tests.py <build_dir> <test_name>
# Example:
# python3 run_tests.py build one_cube
# python3 run_tests.py build one_sphere
# python3 run_tests.py build 001
# python3 run_tests.py build 011

if len(sys.argv) < 3:
  print('Error: please specify the test case name.')
  sys.exit(-1)

build_dir = shlex.quote(sys.argv[1])
test_name = sys.argv[2]

def run_test(cmd):
  ret = os.system(cmd)
  if os.WIFEXITED(ret):
    exit_code = os.WEXITSTATUS(ret)
  else:
    exit_code = 1
  if exit_code != 0:
    print('Test failed with exit code %d' % exit_code)
    sys.exit(exit_code)

if test_name == 'one_cube':
  run_test('python3 main.py --builddir %s --outdir output/one_cube --mesh example/one_cube/csg_low_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'rotated_cuboid':
  run_test('python3 main.py --builddir %s --outdir output/rotated_cuboid --mesh example/rotated_cuboid/csg_low_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'two_cuboids':
  run_test('python3 main.py --builddir %s --outdir output/two_cuboids --mesh example/two_cuboids/csg_low_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'one_sphere':
  run_test('python3 main.py --builddir %s --outdir output/one_sphere --mesh example/one_sphere/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'one_cylinder':
  run_test('python3 main.py --builddir %s --outdir output/one_cylinder --mesh example/one_cylinder/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'rotated_cylinder':
  run_test('python3 main.py --builddir %s --outdir output/rotated_cylinder --mesh example/rotated_cylinder/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'three_cuboids_one_cylinder':
  run_test('python3 main.py --builddir %s --outdir output/three_cuboids_one_cylinder --mesh example/three_cuboids_one_cylinder/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'torus':
  run_test('python3 main.py --builddir %s --outdir output/torus --mesh example/torus/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'torus_cube':
  run_test('python3 main.py --builddir %s --outdir output/torus_cube --mesh example/torus_cube/csg_high_res.off --eps 0.1 --surfacedensity 400 --volumedensity 100' % build_dir)
elif test_name == 'single_torus':
  run_test('python3 main.py --builddir %s --outdir output/single_torus --mesh example/single_torus/csg_high_res.off --eps 0.1 --surfacedensity 40 --volumedensity 10' % build_dir)
elif test_name == 'spot':
  run_test('python3 main.py --builddir %s --outdir output/spot --mesh example/spot/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100 --timeout 180' % build_dir)
elif test_name == 'double_torus':
  run_test('python3 main.py --builddir %s --outdir output/double_torus --mesh example/double_torus/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'bunny':
  run_test('python3 main.py --builddir %s --outdir output/bunny --mesh example/bunny/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'ex_163':
  run_test('python3 main.py --builddir %s --outdir output/ex_163 --mesh example/163/csg_high_res.off --eps 0.05 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_164':
  run_test('python3 main.py --builddir %s --outdir output/ex_164 --mesh example/164/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'ex_165':
  run_test('python3 main.py --builddir %s --outdir output/ex_165 --mesh example/165/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 100' % build_dir)
elif test_name == 'ex_166':
  run_test('python3 main.py --builddir %s --outdir output/ex_166 --mesh example/166/csg_high_res.off --eps 0.05 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_167':
  run_test('python3 main.py --builddir %s --outdir output/ex_167 --mesh example/167/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_168':
  run_test('python3 main.py --builddir %s --outdir output/ex_168 --mesh example/168/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_169':
  run_test('python3 main.py --builddir %s --outdir output/ex_169 --mesh example/169/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_170':
  run_test('python3 main.py --builddir %s --outdir output/ex_170 --mesh example/170/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_171':
  run_test('python3 main.py --builddir %s --outdir output/ex_171 --mesh example/171/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_172':
  run_test('python3 main.py --builddir %s --outdir output/ex_172 --mesh example/172/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_173':
  run_test('python3 main.py --builddir %s --outdir output/ex_173 --mesh example/173/csg_high_res.off --eps 0.02 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'ex_174':
  run_test('python3 main.py --builddir %s --outdir output/ex_174 --mesh example/174/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_175':
  run_test('python3 main.py --builddir %s --outdir output/ex_175 --mesh example/175/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_176':
  run_test('python3 main.py --builddir %s --outdir output/ex_176 --mesh example/176/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'base':
  run_test('python3 main.py --builddir %s --outdir output/base --mesh example/base/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 25' % build_dir)
elif test_name == 'ex_162':
  run_test('python3 main.py --builddir %s --outdir output/162 --mesh example/162/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 25' % build_dir)
elif test_name == 'hallway':
  run_test('python3 main.py --builddir %s --outdir output/hallway --mesh example/hallway/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 100' % build_dir)
elif test_name == 'ex_161':
  run_test('python3 main.py --builddir %s --outdir output/161 --mesh example/161/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 25' % build_dir)
elif test_name == 'ex_160':
  run_test('python3 main.py --builddir %s --outdir output/ex_160 --mesh example/160/csg_high_res.off --initsample 100 --countersample 100 --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_011':
  run_test('python3 main.py --builddir %s --outdir output/ex_011 --mesh example/011/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_023':
  run_test('python3 main.py --builddir %s --outdir output/ex_023 --mesh example/023/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25 --timeout 1800' % build_dir)
elif test_name == 'ex_039':
  run_test('python3 main.py --builddir %s --outdir output/ex_039 --mesh example/039/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_040':
  run_test('python3 main.py --builddir %s --outdir output/ex_040 --mesh example/040/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_041':
  run_test('python3 main.py --builddir %s --outdir output/ex_041 --mesh example/041/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_043':
  run_test('python3 main.py --builddir %s --outdir output/ex_043 --mesh example/043/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_045':
  run_test('python3 main.py --builddir %s --outdir output/ex_045 --mesh example/045/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_046':
  run_test('python3 main.py --builddir %s --outdir output/ex_046 --mesh example/046/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_050':
  run_test('python3 main.py --builddir %s --outdir output/ex_050 --mesh example/050/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_054':
  run_test('python3 main.py --builddir %s --outdir output/ex_054 --mesh example/054/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_056':
  run_test('python3 main.py --builddir %s --outdir output/ex_056 --mesh example/056/csg_high_res.off --eps 0.02 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_057':
  run_test('python3 main.py --builddir %s --outdir output/ex_057 --mesh example/057/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_059':
  run_test('python3 main.py --builddir %s --outdir output/ex_059 --mesh example/059/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_060':
  run_test('python3 main.py --builddir %s --outdir output/ex_060 --mesh example/060/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_062':
  run_test('python3 main.py --builddir %s --outdir output/ex_062 --mesh example/062/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_065':
  run_test('python3 main.py --builddir %s --outdir output/ex_065 --mesh example/065/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_066':
  run_test('python3 main.py --builddir %s --outdir output/ex_066 --mesh example/066/csg_high_res.off --eps 0.02 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_067':
  run_test('python3 main.py --builddir %s --outdir output/ex_067 --mesh example/067/csg_high_res.off --eps 0.05 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_068':
  run_test('python3 main.py --builddir %s --outdir output/ex_068 --mesh example/068/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_069':
  run_test('python3 main.py --builddir %s --outdir output/ex_069 --mesh example/069/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_072':
  run_test('python3 main.py --builddir %s --outdir output/ex_072 --mesh example/072/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_074':
  run_test('python3 main.py --builddir %s --outdir output/ex_074 --mesh example/074/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_075':
  run_test('python3 main.py --builddir %s --outdir output/ex_075 --mesh example/075/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_078':
  run_test('python3 main.py --builddir %s --outdir output/ex_078 --mesh example/081/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_079':
  run_test('python3 main.py --builddir %s --outdir output/ex_079 --mesh example/079/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_081':
  run_test('python3 main.py --builddir %s --outdir output/ex_081 --mesh example/081/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_082':
  run_test('python3 main.py --builddir %s --outdir output/ex_082 --mesh example/082/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_090':
  run_test('python3 main.py --builddir %s --outdir output/ex_090 --mesh example/090/csg_high_res.off --eps 0.05 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_091':
  run_test('python3 main.py --builddir %s --outdir output/ex_091 --mesh example/091/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_096':
  run_test('python3 main.py --builddir %s --outdir output/ex_096 --mesh example/096/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_098':
  run_test('python3 main.py --builddir %s --outdir output/ex_098 --mesh example/098/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_101':
  run_test('python3 main.py --builddir %s --outdir output/ex_101 --mesh example/101/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_102':
  run_test('python3 main.py --builddir %s --outdir output/ex_102 --mesh example/102/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_103':
  run_test('python3 main.py --builddir %s --outdir output/ex_103 --mesh example/105/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_104':
  run_test('python3 main.py --builddir %s --outdir output/ex_104 --mesh example/104/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_105':
  run_test('python3 main.py --builddir %s --outdir output/ex_105 --mesh example/105/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_106':
  run_test('python3 main.py --builddir %s --outdir output/ex_106 --mesh example/106/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_107':
  run_test('python3 main.py --builddir %s --outdir output/ex_107 --mesh example/107/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_108':
  run_test('python3 main.py --builddir %s --outdir output/ex_108 --mesh example/108/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_109':
  run_test('python3 main.py --builddir %s --outdir output/ex_109 --mesh example/109/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_111':
  run_test('python3 main.py --builddir %s --outdir output/ex_111 --mesh example/111/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_112':
  run_test('python3 main.py --builddir %s --outdir output/ex_112 --mesh example/112/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_114':
  run_test('python3 main.py --builddir %s --outdir output/ex_114 --mesh example/114/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_115':
  run_test('python3 main.py --builddir %s --outdir output/ex_115 --mesh example/115/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_117':
  run_test('python3 main.py --builddir %s --outdir output/ex_117 --mesh example/117/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_118':
  run_test('python3 main.py --builddir %s --outdir output/ex_118 --mesh example/118/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_122':
  run_test('python3 main.py --builddir %s --outdir output/ex_122 --mesh example/122/csg_high_res.off --eps 0.01 --surfacedensity 2000 --volumedensity 50' % build_dir)
elif test_name == 'ex_123':
  run_test('python3 main.py --builddir %s --outdir output/ex_123 --mesh example/123/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_126':
  run_test('python3 main.py --builddir %s --outdir output/ex_126 --mesh example/126/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_127':
  run_test('python3 main.py --builddir %s --outdir output/ex_127 --mesh example/127/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_128':
  run_test('python3 main.py --builddir %s --outdir output/ex_128 --mesh example/128/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_129':
  run_test('python3 main.py --builddir %s --outdir output/ex_129 --mesh example/129/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_130':
  run_test('python3 main.py --builddir %s --outdir output/ex_130 --mesh example/130/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_131':
  run_test('python3 main.py --builddir %s --outdir output/ex_131 --mesh example/131/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_133':
  run_test('python3 main.py --builddir %s --outdir output/ex_133 --mesh example/133/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_134':
  run_test('python3 main.py --builddir %s --outdir output/ex_134 --mesh example/134/csg_high_res.off --eps 0.05 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_139':
  run_test('python3 main.py --builddir %s --outdir output/ex_139 --mesh example/139/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_140':
  run_test('python3 main.py --builddir %s --outdir output/ex_140 --mesh example/140/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 50' % build_dir)
elif test_name == 'ex_142':
  run_test('python3 main.py --builddir %s --outdir output/ex_142 --mesh example/142/csg_high_res.off --eps 0.01 --surfacedensity 2000 --volumedensity 50' % build_dir)
elif test_name == 'ex_143':
  run_test('python3 main.py --builddir %s --outdir output/ex_143 --mesh example/143/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_144':
  run_test('python3 main.py --builddir %s --outdir output/ex_144 --mesh example/144/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_145':
  run_test('python3 main.py --builddir %s --outdir output/ex_145 --mesh example/145/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_146':
  run_test('python3 main.py --builddir %s --outdir output/ex_146 --mesh example/146/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_147':
  run_test('python3 main.py --builddir %s --outdir output/ex_147 --mesh example/147/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_148':
  run_test('python3 main.py --builddir %s --outdir output/ex_148 --mesh example/148/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_150':
  run_test('python3 main.py --builddir %s --outdir output/ex_150 --mesh example/150/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_151':
  run_test('python3 main.py --builddir %s --outdir output/ex_151 --mesh example/151/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_152':
  run_test('python3 main.py --builddir %s --outdir output/ex_152 --mesh example/152/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_153':
  run_test('python3 main.py --builddir %s --outdir output/ex_153 --mesh example/153/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 25 --timeout 600' % build_dir)
elif test_name == 'ex_155':
  run_test('python3 main.py --builddir %s --outdir output/ex_155 --mesh example/155/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_156':
  run_test('python3 main.py --builddir %s --outdir output/ex_156 --mesh example/156/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_157':
  run_test('python3 main.py --builddir %s --outdir output/ex_157 --mesh example/157/csg_high_res.off --eps 0.1 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_158':
  run_test('python3 main.py --builddir %s --outdir output/ex_158 --mesh example/158/csg_high_res.off --eps 0.1 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_159':
  run_test('python3 main.py --builddir %s --outdir output/ex_159 --mesh example/159/csg_high_res.off --eps 0.025 --surfacedensity 250 --volumedensity 25' % build_dir)
else:
  print('Unknown test case: %s' % test_name)
  sys.exit(-1)
