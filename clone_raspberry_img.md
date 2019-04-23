# Clone raspberry image from a SD card to another one

Installation process coming from the [thepihut website](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card)
```
## Using linux:


Before inserting the SD card into the reader on your Linux PC, run the following command to find out which devices are currently available:

_df -h_

Which will return something like this:

_Filesystem 1K-blocks Used Available Use% Mounted on_
_rootfs 29834204 15679020 12892692 55% /_
_/dev/root 29834204 15679020 12892692 55% /_
_devtmpfs 437856 0 437856 0% /dev_
_tmpfs 88432 284 88148 1% /run_
_tmpfs 5120 0 5120 0% /run/lock_
_tmpfs 176860 0 176860 0% /run/shm_
_/dev/mmcblk0p1 57288 14752 42536 26% /boot_



Insert the SD card into a card reader and use the same df -h command to find out what is now available:

_Filesystem 1K-blocks Used Available Use% Mounted on_
_rootfs 29834204 15679020 12892692 55% /_
_/dev/root 29834204 15679020 12892692 55% /_
_devtmpfs 437856 0 437856 0% /dev_
_tmpfs 88432 284 88148 1% /run_
_tmpfs 5120 0 5120 0% /run/lock_
_tmpfs 176860 0 176860 0% /run/shm_
_/dev/mmcblk0p1 57288 14752 42536 26% /boot_
_/dev/sda5 57288 9920 47368 18% /media/boot_
_/dev/sda6 6420000 2549088 3526652 42% /media/41cd5baa-7a62-4706-b8e8-02c43ccee8d9_



The new device that wasn't there last time is your SD card.

The left column gives the device name of your SD card, and will look like '/dev/mmcblk0p1' or '/dev/sdb1'. The last part ('p1' or '1') is the partition number, but you want to use the whole SD card, so you need to remove that part from the name leaving '/dev/mmcblk0' or '/dev/sdb' as the disk you want to read from.

Open a terminal window and use the following to backup your SD card:

	_sudo dd if=/dev/sdb of=~/SDCardBackup.img_



As on the Mac, the dd command does not show any feedback so you just need to wait until the command prompt re-appears.

To restore the image, do exactly the same again to discover which device is your SD card.  As with the Mac, you need to unmount it first, but this time you need to use the partition number as well (the 'p1' or '1' after the device name).  If there is more than one partition on the device, you will need to repeat the umount command for all partition numbers.  For example, if the df -h shows that there are two partitions on the SD card, you will need to unmount both of them:


	_sudo umount /dev/sdb1_
	_sudo umount /dev/sdb2_


Now you are able to write the original image to the SD drive:

	_sudo dd bs=4M if=~/SDCardBackup.img of=/dev/sdb_


The bs=4M option sets the 'block size' on the SD card to 4Meg.  If you get any warnings, then change this to 1M instead, but that will take a little longer to write.

Again, wait while it completes.  Before ejecting the SD card, make sure that your Linux PC has completed writing to it using the command:

	_sudo sync_
