@echo off

echo =====================================
echo Building TemplateMapper...
echo =====================================

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist TemplateMapper.spec del TemplateMapper.spec

pyinstaller ^
--name TemplateMapper ^
--onefile ^
--windowed ^
--icon=assets/icons/app_icon.ico ^
main.py

echo.
echo =====================================
echo Build Complete!
echo =====================================
echo.
echo Executable:
echo dist\TemplateMapper.exe
echo.

pause