[app]
title = Aura Engine
package.name = auraengine
package.domain = org.aura
source.include_exts = py,png,jpg,kv,atlas,glsl,obj,gltf
version = 1.0
requirements = python3,kivy,requests,moderngl,overpy,numpy==1.26.4,pillow
orientation = landscape
fullscreen = 1
android.archs = arm64-v8a
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
source.dir = .
android.accept_sdk_license = True
# force
android.ndk = 25b
log_level = 2
