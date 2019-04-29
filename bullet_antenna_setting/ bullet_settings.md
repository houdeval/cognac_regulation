# Install bullet antenna to allow a long-distance communication between a computer and the Raspberry circuit board of the float

Here, the bullet will be used as a router, that is to say many devices will be able to connect to the antenna so as to be part of a same network. The aim is to access the Raspberry circuit board easily, up to 52.3 km far from the antenna if the Raspberry is equipped with such an emitter.

## Settings :

To set the antenna considering that the IP or the password to access the antenna setting page are unknown :

* First, connect both network cables to the adaptator : PWR+DATA OUT is dedicated to the antenna and DATA iN is dedicated to the computer.

* Afterwards, keep pushing the Reset button under the antenna support (about 30 sec) until the light are blinking.

* Then, set your wired connection so as to connect to the antenna whose IP address should be 192.168.1.20 .

With this aim in mind, you has to set a fixed IP address for your computer, compatible with this network such as 192.168.1.21 .

Just fill the fields as in the screenshot below, in the IPv4 tab to choose the configuration previously described.

![Bullet_reset](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/bullet_reset.png)

* Then open your internet browser and write the IP address of the antenna in the search bar as below. A user name and a password will be required to continue, by default, both should be "ubnt".

![Bullet_setting_page](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/bullet_setting_page.png)

* Next, fill the different fields to configure the antenna as in the following screenshots.


Note that you can change the distance range of the antenna as you prefer in the section "ADVANCED". This distance also depends on the country code you chose in the "WIRELESS" section.


Note that the settings for the choice of IP address family is in the network section for the suggested following settings, the IP address class is 192.168.0.X where the IP address of the antenna is 192.168.0.20 .


Do not forget to save changes at the bottom of the page, but you must apply the changes only at the end of the setting process.


If you want to complete this step faster, you can directly load the file "XM-687251684A4D.cfg" thanks to the "Tools" tab on the setting page.


![Airmax_section](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/airmax_section.png)

![Main_section](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/main_section.png)

![Wireless_section](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/wireless_section.png)

![Network_section](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/network_section.png)

![Advanced_section](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/advanced_section.png)

![Services_section1](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/services_section1.png)

![Services_section2](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/services_section2.png)

![System_section1](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/system_section1.png)

![System_section2](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/system_section2.png)

* Then, in such a configuration, after applying the modifications, you should be able to detect the WIFI network related to the antenna whose name was defined here as "seabot". You should not need to keep connecting by cables between the antenna and the computer. Set you computer network parameters as below to be able to connect to this new network. Note that the IP address 192.168.0.40 could be any address of the form 192.168.0.X except 192.168.0.0, 192.168.0.255, 192.168.0.20, 192.168.0.1 .

![WIFI_config](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/WIFI_config.png)

* Now, you should be able to connect to the antenna as a router. To check the connection, just try to write the address of the antenna (192.168.0.20) in your browser to access the setting page. To connect the raspberry, set the same network configuration with a different IP address from the computer.


* If you still face problems :
- Try to plug and unplug the different cables.
- Try to connect to the antenna with your computer by cables with this kind of configuration :
![Wired_config](https://github.com/houdeval/cognac_regulation/bullet_antenna_setting/wired_config.png)
- Check whether you chose the right parameters.
- Check if the IP address class used is compatible with your Raspberry circuit board.
- Restart your computer.
- Reset the antenna and do this tutorial again from the beginning.
