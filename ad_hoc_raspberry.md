# Creating an Ad-Hoc network in the Raspberry Pi to connect a PC to the Raspberry Pi directly



1. Save a copy of the file /etc/network/interfaces not to lose the current settings for other applications :
```
cp /etc/network/interfaces /etc/network/copy-interfaces
```


2. Then replace the file with the following content

```
nano /etc/network/interfaces

auto wlan0
iface wlan0 inet static
     address 192.168.0.13
     netmask 255.255.255.0
     wireless-channel 1
     wireless-essid seaboat
     wireless-mode ad-hoc
```


3. Reboot the Raspberry Pi.


4. The network will appear in the computer in the list of wireless 
networks. Connect to it.


5. Add a static IP address to the Mac/PC with 
192.168.0.X/255.255.255.0 where X can belong to the interval [1, 254] except 13 (address dedicated to the Raspberry Pi). This step is necessary because there is no DHCP server in the Raspberry Pi.


6. Then you can ssh to the Raspberry Pi to  pi@192.168.0.13 from your computer.

```
ssh pi@192.168.0.13
```


Source : [Ad-Hoc settings website](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=29&t=39927)


