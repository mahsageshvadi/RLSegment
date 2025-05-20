cmake_minimum_required(VERSION 3.10)
project(VESCL_Python)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include FetchContent for downloading dependencies
include(FetchContent)

# Fetch and build pybind11
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.11.1  # Use a stable version
)
FetchContent_MakeAvailable(pybind11)

# Find Python
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Add the main VESCL library
add_subdirectory(Source)

# Create the Python module
pybind11_add_module(vescl_binding vescl_binding.cpp)

# Link against the VESCL library
target_link_libraries(vescl_binding PRIVATE VESCL)

# Include directories
target_include_directories(vescl_binding PRIVATE
    ${CMAKE_SOURCE_DIR}/Source
    ${Python_INCLUDE_DIRS}
) 