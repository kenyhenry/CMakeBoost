
cmake_minimum_required(VERSION 3.10)
project(MyProject VERSION 1.0.0)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add dependencies

# opengl
add_subdirectory(libs/opengl)

# glfw
add_subdirectory(libs/glfw)

# Add the executable
add_executable(MyProject src/main.cpp)

# Link dependencies

target_link_libraries(MyProject PRIVATE opengl)

target_link_libraries(MyProject PRIVATE glfw)
