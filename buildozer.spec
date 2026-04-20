[app]
title = Galaxy
package.name = galaxyv3
package.domain = org.galaxy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,ttf
source.include_patterns = audio/*.wav,fonts/*.ttf,images/*.jpg,*.kv

version = 3.0

requirements = python3,kivy==2.3.0,Cython==0.29.33

orientation = landscape
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1
