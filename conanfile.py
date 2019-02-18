from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1.0"
    license = "LICENSE"
    author = "James, modified by Hopobcn"
    url = "https://github.com/Hopobcn/hello"
    description = "Simple library to test conan"
    topics = ("conan", "cmake", "cpp")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/Hopobcn/hello.git -b master")
        self.run("cd hello")


    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hello")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello/include")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

