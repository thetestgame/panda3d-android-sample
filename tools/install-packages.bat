@echo off
cd ../

rem Install the packages.apks file via adb. 
java -jar .\tools\bundletool.jar install-apks --apks .\packages.apks