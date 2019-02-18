# GOOD CMake documentation: https://cliutils.gitlab.io/modern-cmake/
cmake_minimum_required(VERSION 3.9..3.12)

if (${CMAKE_VERSION} VERSION_LESS 3.12)
    cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
else ()
    cmake_policy(VERSION 3.12)
endif ()
# CMake versions info https://cliutils.gitlab.io/modern-cmake/chapters/intro/newcmake.html

project(MyHello VERSION 1.0.0
                DESCRIPTION "Library hello (conan example)"
                LANGUAGES CXX)

# Include helper modules to CMake path
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

# IDE support: Xcode & VS require folder support for correctly displaying project hierarchy
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

add_subdirectory(src)
add_subdirectory(test)

# Report summary of packages found
include(FeatureSummary)
if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
    feature_summary(WHAT ENABLED_FEATURES DISABLED_FEATURES PACKAGES_FOUND)
    feature_summary(FILENAME ${CMAKE_CURRENT_BINARY_DIR}/features.log WHAT ALL)
endif()

#--------------------------------------------
# Exporting and installing
#--------------------------------------------

# Run 'make install' to install all targets on CMAKE_INSTALL_PREFIX:PATH directory

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    helloConfigVersion.cmake
    VERSION ${PACKAGE_VERSION}
    COMPATIBILITY AnyNewerVersion
)

install(EXPORT helloTargets
    FILE helloTargets.cmake
    NAMESPACE say::
    DESTINATION lib/cmake/
)
