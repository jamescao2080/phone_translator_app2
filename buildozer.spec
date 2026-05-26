[app]
title = AI 同声传译
package.name = aitranslator
package.domain = org.manus
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,requests,googletrans==4.0.0-rc1,SpeechRecognition,pyttsx3,pyjnius,plyer
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = RECORD_AUDIO, INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
