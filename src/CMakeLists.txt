CMAKE_MINIMUM_REQUIRED(VERSION 3.10.2)


PROJECT(HelloWorld)
include_directories(include)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


ADD_LIBRARY(my_hello "my_hello.cpp")

#adding shared library
#ADD_LIBRARY(hello_shared SHARED "my_hello_shared.cpp")

ADD_EXECUTABLE(hello main.cpp)
target_link_libraries(hello my_hello)


message(STATUS ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})

install(TARGETS hello CONFIGURATIONS Release RUNTIME DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/bin)
install(TARGETS my_hello DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/lib)
#install(TARGETS hello_shared DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/lib_shared)
