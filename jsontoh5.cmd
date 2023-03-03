@echo off
set PYTHON_DIR=%USERPROFILE%\Downloads\python-3.10.8-amd64-portable\
set PATH=%PYTHON_DIR%;%PYTHON_DIR%Scripts

jsontoh5.exe ./sample.json ./new-sample.h5
pause
