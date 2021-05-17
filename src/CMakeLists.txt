CMAKE_MINIMUM_REQUIRED(VERSION 3.10.2)


PROJECT(HelloWorld)
include_directories(include)

#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()


ADD_LIBRARY(hello "my_hello.cpp")

#adding shared library
ADD_LIBRARY(hello_shared SHARED "my_hello_shared.cpp")

ADD_EXECUTABLE(greet main.cpp)
target_link_libraries(greet hello hello_shared)


message(STATUS ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})

install(TARGETS greet DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/bin)
install(TARGETS hello DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/lib)
install(TARGETS hello_shared DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/lib_shared)
