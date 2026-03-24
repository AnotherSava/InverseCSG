cmake_minimum_required(VERSION 3.1)

project(csg_cpp_command)

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(UNIX)
  add_definitions("-Wall")
elseif(MSVC)
  add_definitions("-D_CRT_SECURE_NO_WARNINGS")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /bigobj")
endif()

# Eigen: prefer system install, fall back to vendored copy.
find_package(Eigen3 QUIET)
if(Eigen3_FOUND AND TARGET Eigen3::Eigen)
  message(STATUS "Using system Eigen3: ${Eigen3_DIR}")
else()
  message(STATUS "System Eigen3 not found, using vendored lib/eigen-3.3.4")
  include_directories(lib/eigen-3.3.4)
endif()
# gco.
include_directories(lib/gco-v3.0)
add_subdirectory(lib/gco-v3.0)
# CGAL (>= 5.0 required).
find_package(CGAL 5.0 QUIET)
if(NOT CGAL_FOUND)
  message(FATAL_ERROR "CGAL not found. Install with: sudo apt-get install libcgal-dev")
endif()

set(SRC_DIR "src/")
include_directories(${SRC_DIR})
file(GLOB_RECURSE CPP_HEADERS ${SRC_DIR}*.h)
file(GLOB_RECURSE CPP_FILES ${SRC_DIR}*.cpp)
add_executable(csg_cpp_command ${CPP_FILES} ${CPP_HEADERS})
target_link_libraries(csg_cpp_command gco)
if(Eigen3_FOUND AND TARGET Eigen3::Eigen)
  target_link_libraries(csg_cpp_command Eigen3::Eigen)
endif()
target_link_libraries(csg_cpp_command CGAL::CGAL)
