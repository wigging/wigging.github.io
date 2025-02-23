---
title: CMake build and install
date: December 13, 2022
---

Use CMake to build and/or install code for a C++ project. The build and install steps are discussed individually in each section below. This discussion assumes a project structure as shown in the file tree diagram.

```text
MyProject/
├── CMakeLists.txt
└── src/
    ├── adder.cpp
    ├── adder.h
    └── main.cpp
```

## Build steps

In this example, the `CMakeLists.txt` file contains instructions for building the project using the CMake command line tool:

```text
cmake_minimum_required(VERSION 3.2)

project(AdderExample LANGUAGES CXX)

add_executable(AdderExample src/main.cpp src/adder.cpp)
```

Use the commands shown here to build the project with CMake. After building the project, the executable named `AdderExample` is available in the build directory.

```bash
# Configure the project and generate a native build system
# This creates a directory named `build`
cd MyProject
cmake -S . -B build

# Call the build system to compile/link the project
cmake --build build

# Run the executable
./build/AdderExample
```

The structure of the project after running the build command is shown below.

```text
MyProject/
├── CMakeLists.txt
├── build/
│   ├── AdderExample
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   ├── Makefile
│   └── cmake_install.cmake
└── src
    ├── adder.cpp
    ├── adder.h
    └── main.cpp
```

Remove the build directory to clear the project of built files and other output generated from CMake.

```console
$ rm -rf build
```

## Install steps

For this example, the `CMakeLists.txt` file contains instructions for building and installing the project using the CMake command line tool:

```text
cmake_minimum_required(VERSION 3.2)

project(AdderExample LANGUAGES CXX)

add_executable(AdderExample src/main.cpp src/adder.cpp)

install(TARGETS AdderExample)
```

Use the commands shown here to build and install the project with CMake. After installing the project, the executable named `AdderExample` is available from the command line.

```bash
# Configure the project and generate a native build system
cmake -S . -B build

# Call the build system to compile/link the project
cmake --build build

# Install the executable to usr/local/bin
cmake --install build

# Run the executable, assumes usr/local/bin is in your path
AdderExample
```

The structure of the project after running the Cmake commands is shown below. The `install_manifest.txt` in the build directory lists all the files installed on the machine.

```text
MyProject/
├── CMakeLists.txt
├── build/
│   ├── AdderExample
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   ├── Makefile
│   ├── cmake_install.cmake
│   └── install_manifest.txt
└── src/
    ├── adder.cpp
    ├── adder.h
    └── main.cpp
```

Remove the build directory to clear the project of built files and other output generated from the build process. Also, remove the files listed in the `install_manifest.txt` file to cleanup files generated from the install process.

```bash
# Remove the build directory
rm -rf build

# Remove installed files
cat build/install_manifest.txt | xargs rm
```
