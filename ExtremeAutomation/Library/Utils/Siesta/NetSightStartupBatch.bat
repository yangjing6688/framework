ping 127.0.0.1 -n 5

pip install psutil

ping 127.0.0.1 -n 2

pip install flask_cors

ping 127.0.0.1 -n 2

if not exist "C:\Automation" rd /s /q C:\Automation
	mkdir C:\Automation

ping 127.0.0.1 -n 2

bitsadmin.exe /transfer "Transfer Rest Server Start..." http://10.52.15.200/files/DEV/RestServerStart.py C:\Automation\RestServerStart.py

ping 127.0.0.1 -n 2

python C:\Automation\RestServerStart.py %*

ping 127.0.0.1 -n 2

cd %C:\Automation\RestServer\%

ping 127.0.0.1 -n 2

python C:\Automation\RestServer\RestServer.py %*

pause