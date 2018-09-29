@echo off

set LARGEPICDIR=d:\Github\_Pics\Large
set SMALLPICSDIR=d:\Github\_Pics\Small
set CONVERT_DIR=d:\kits\NConvert-win64\XnView
set SEVENZIPPATH="c:\Program Files\7-Zip"
set PICS_ZIP_PATH=d:\Github\_Pics
set CARS_DIR=d:\Github\jbcars\AddCars\pics

set CAR_DIR=%CARS_DIR%\car105
set PERCENT_SIZE=25%%

@rem remove existing pics
pushd %LARGEPICDIR%
for %%i in (*.*) do (
	del /F /Q "%%i"
)
popd
pushd %SMALLPICSDIR%
for %%i in (*.*) do (
	del /F /Q "%%i"
)
popd

@rem unarchive zip
%SEVENZIPPATH%\7z.exe e %PICS_ZIP_PATH%\*.zip -o%LARGEPICDIR%

@rem convert pics
pushd %LARGEPICDIR%
for %%i in (*.*) do (
	%CONVERT_DIR%\nconvert.exe -o "%SMALLPICSDIR%\%%i" -resize %PERCENT_SIZE% %PERCENT_SIZE% "%%i"
)
popd	

@rem goto END

@rem -------------------------------------------------------------------------
@rem copy small pics to car dir
if not exist %CAR_DIR% mkdir %CAR_DIR%
pushd %CAR_DIR%
for %%i in (*.*) do (
	del /F /Q "%%i"
)
popd

pushd %SMALLPICSDIR%
xcopy /R /F /Y *.* %CAR_DIR%
popd

:END