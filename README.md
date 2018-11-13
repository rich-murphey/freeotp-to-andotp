# freeotp-to-andotp
migrate from freeotp+ to andotp

This is a python script that converts a freeotp backup into an
import for andotp.

<img
src="https://raw.githubusercontent.com/rich-murphey/freeotp-to-andotp/master/doc/freeotp_export_screenshot.gif"
width="40%" align="right">
# Export from Freeotp+ 
For example, one can export a backup from freeotp+ as shown on the
right. This will create a file "freeotp-backup.json", typically in the "Downloads" folder.

Next, upload "freeotp-backup.json" to your computer, for example using any of:
* [xplore file manager](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore) over ssh or smb
* Google drive
* Dropbox

Then, use the python script to convert it to a andotp backup:

    freeotp-to-andotp.py freeotp-backup.json >andotp-backup.json

<img
src="https://raw.githubusercontent.com/rich-murphey/freeotp-to-andotp/master/doc/andotp-backup-screenshot.gif"
width="40%" align="right"> 
# Import into andotp
Last, download andotp-backup.json to your device, and import it
into andotp as shown on the right.

# Credits
This is based on [freeotp-to-andotp-migrator](https://gitlab.com/stavros/freeotp-to-andotp-migrator) by [Stavros Korokithakis](https://gitlab.com/stavros), which reads XML format freeotp data.
