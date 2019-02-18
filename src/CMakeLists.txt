add_library(hello STATIC hello.cpp)
add_library(say::hello ALIAS hello)

target_include_directories(hello
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_compile_features(hello PRIVATE cxx_std_17)
set_target_properties(hello PROPERTIES CXX_EXTENSIONS OFF)
set_target_properties(hello PROPERTIES PUBLIC_HEADER "hello.h")

install(TARGETS hello
    EXPORT helloTargets
    LIBRARY DESTINATION lib COMPONENT libraries
    ARCHIVE DESTINATION lib COMPONENT libraries
    RUNTIME DESTINATION bin COMPONENT binaries
    PUBLIC_HEADER DESTINATION include COMPONENT headers
    INCLUDES DESTINATION include
)