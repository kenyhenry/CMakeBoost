# CMakeBoost

CMakeBoost is a tool designed to simplify dependency management, compilation, and execution of C/C++ projects using CMake and a YAML configuration file.
You can compile minimal project, with minimum files without compiling/including the whole library, but if you want to compile the whole library enjoy :)

## Features

- Define project dependencies, entry points, and build configurations in a simple YAML file.
- Automatically download and build dependencies.
- Generate `CMakeLists.txt` files.
- Compile and run your project with a single command.
- compile only file you want to include in your project without including the whole library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CMakeBoost.git
   cd CMakeBoost
