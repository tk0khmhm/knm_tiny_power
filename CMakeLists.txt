cmake_minimum_required(VERSION 2.8.3)
project(knm_tiny_power)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -g -O2")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  cereal_catkin
  knm_tiny_msgs
  nav_msgs
  geometry_msgs
  tf
)

find_package(Boost REQUIRED COMPONENTS thread)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  #CATKIN_DEPENDS
  #DEPENDS
)

###########
## Build ##
###########

include_directories(include
  ${catkin_INCLUDE_DIRS}
)


add_library(knm_tiny_lib src/knm_tiny_lib.cpp)
target_link_libraries(knm_tiny_lib
  ${catkin_LIBRARIES}
)

add_executable(knm_tiny_joy src/knm_tiny_joy.cpp)
target_link_libraries(knm_tiny_joy
  ${catkin_LIBRARIES}
)

add_executable(knm_tiny_power src/knm_tiny_power.cpp)
target_link_libraries(knm_tiny_power cereal_catkin knm_tiny_lib)

add_executable(tf_for_bag src/tf_for_bag.cpp)
target_link_libraries(tf_for_bag
  ${catkin_LIBRARIES}
)

#add_executable(knm_tiny_power_calibration src/knm_tiny_power_calibration.cpp)
#target_link_libraries(knm_tiny_power_calibration cereal_catkin knm_tiny_lib)

