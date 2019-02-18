add_executable(greet test.cpp)
target_link_libraries(greet say::hello)