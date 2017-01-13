# rasp_temp
Rasperry
Run Python script in backgroud
#copy the serive to systemd

$ sudo cp thermo.service /lib/systemd/system

#Enable service

$ sudo systemctl daemon-reload
$ sudo systemctl enable thermo.service
$ sudo systemctl start thermo.servie

# stop service
$ sudo systemctl stop thermo.service

# verify status of service

$ sudo systemctl status thermo.service

OR

$ tail -f /var/log/syslog
