# Conan recipe for nvidia-cg-toolkit-binaries 3.1.0013

[![Build Status: Windows](https://ci.appveyor.com/api/projects/status/github/KonradNoTantoo/nvidia-cg-toolkit-binaries_conan?svg=true)](https://ci.appveyor.com/project/KonradNoTantoo/nvidia-cg-toolkit-binaries-conan)

[![Build Status: Linux](https://api.travis-ci.org/KonradNoTantoo/nvidia-cg-toolkit-binaries_conan.svg?branch=master)](https://travis-ci.org/KonradNoTantoo/nvidia-cg-toolkit-binaries_conan)

### Description
Downloads library archive and adds headers, libraries and executables to conan data cache. Adds executable dir to path. For Windows, NVidia only offers an opaque .exe installer. Until someone finds a way to extract libs from that installer, we have to start from a repackaged archive made available on Utopia bintray. This is possible under NVidia's license for their CG toolkit which permits redistribution.

NVidia's license for CG is available on their website and in our repackaged tarball for Windows.

### Repository
Published on [Utopia bintray](https://bintray.com/konradnotantoo/utopia/):
```
conan remote add utopia https://api.bintray.com/conan/konradnotantoo/utopia
```

### Recipe license
MIT