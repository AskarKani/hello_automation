from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "hello"
    version = "1.0.0"
    license = "<Put the package license here>"
    author = "Mohamed Askar Kani M"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "src/*"
	

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()
        #cmake.install()

    def package(self):
        #cmake = CMake(self)
        #cmake.configure(source_folder="src")
        #cmake.install()
        self.copy("bin/hello")
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

