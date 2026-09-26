#!/usr/bin/env bash
set -euo pipefail

brew install automake libtool meson nasm ninja pkg-config oras zstd > /dev/null
sudo mdutil -a -i off > /dev/null
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
xcodebuild -version

# upstream ci: no -g in the libraries' debug builds, keeps them small
gnu="$(brew --prefix)/share/cmake/Modules/Compiler/GNU.cmake"
if [ -f "$gnu" ]; then
  sudo sed -i '' '/CMAKE_${lang}_FLAGS_DEBUG_INIT/s/ -g//' "$gnu"
fi

# a universal debug + release prepare takes tens of gigabytes, the other xcodes are the biggest thing to drop
free=$(df -g / | awk 'NR == 2 { print $4 }')
if [ "$free" -lt 60 ]; then
  realpath() { python3 -c 'import os, sys; print(os.path.realpath(sys.argv[1]))' "$1"; }
  keep=$(realpath /Applications/Xcode.app)
  for xcode in /Applications/Xcode_*.app; do
    if [ "$(realpath "$xcode")" != "$keep" ]; then
      sudo rm -rf "$xcode"
    fi
  done
fi
df -h / | tail -n1
