# sys_files
Setup the following startup script:
````
$sudo crontab -e

@reboot sh /home/pi/startup_scripts.sh >/home/pi/logs/cronlog 2>&1
````
