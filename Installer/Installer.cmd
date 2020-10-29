regedit /s "PhotoOrganizer/PhotoOrganizer.reg"
mkdir "C:\Program Files\PhotoOrganizer"
xcopy "PhotoOrganizer" "C:\Program Files\PhotoOrganizer" /F /C /E
@echo off
MSG * Installation complete
exit