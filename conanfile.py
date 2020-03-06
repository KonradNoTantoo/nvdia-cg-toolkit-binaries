from conans import ConanFile, tools, errors
import os


class NvidiacgtoolkitbinariesConan(ConanFile):
	name = "nvidia-cg-toolkit-binaries"
	version = "3.1.0013"
	license = "NVidia EULA"
	author = "konrad.no.tantoo"
	url = "https://github.com/KonradNoTantoo/nvdia-cg-toolkit-binaries"
	description = "NVidia's deprecated programmated shader compiler"
	topics = ("NVidia", "cg", "cg toolkit", "libcg", "conan")
	settings = ["os", "arch"]
	build_policy = "missing"


	def source(self):
		if self.settings.os == "Linux":
			dl_path = "http://developer.download.nvidia.com/cg/Cg_3.1/Cg-3.1_April2012_{}.tgz".format(self.settings.arch)
			tools.get(dl_path)
		elif self.settings.os == "Windows":
			# nvidia distributes only an opaque package for Windows
			dl_path = "https://bintray.com/konradnotantoo/utopia-binaries/download_file?file_path=nvidia-cg-toolkit-3.1.zip"
			tools.get(dl_path, filename="binaries-archive")
		else:
			raise conans.errors.ConanInvalidConfiguration("os='{}' not supported".format(self.settings.os))


	def package(self):
		if self.settings.os == "Linux":
			self.copy("*", dst="bin", src="usr/bin", keep_path=True)
			if self.settings.arch == "x86_64":
				self.copy("*", dst="lib", src="usr/lib64", keep_path=True)
			else:
				self.copy("*", dst="lib", src="usr/lib", keep_path=True)
			self.copy("*", dst="include", src="usr/include", keep_path=True)
			self.copy("*", dst="doc", src="usr/local", keep_path=True)
		elif self.settings.os == "Windows":
			if self.settings.arch == "x86_64":
				self.copy("*", dst="bin", src="bin.x64", keep_path=True)
				self.copy("*", dst="lib", src="lib.x64", keep_path=True)
			else:
				self.copy("*", dst="bin", src="bin", keep_path=True)
				self.copy("*", dst="lib", src="lib", keep_path=True)
			self.copy("*", dst="include", src="include", keep_path=True)
			self.copy("readme.txt", dst="doc", src=".", keep_path=True)
			self.copy("License.txt", dst="doc", src=".", keep_path=True)


	def package_info(self):
		if self.settings.os == "Linux":
			self.cpp_info.libs = ["Cg", "CgGL"]
			self.cpp_info.system_libs = ["dl", "m"]
		elif self.settings.os == "Windows":
			self.cpp_info.libs = ["cg", "cgD3D9", "cgD3D10", "cgD3D11", "cgGL", "glut32"]

		bindir = os.path.join(self.package_folder, "bin")
		self.output.info("Appending PATH environment variable: {}".format(bindir))
		self.env_info.PATH.append(bindir)
