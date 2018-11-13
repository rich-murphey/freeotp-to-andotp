
default: freeotp_to_andotp.py freeotp-backup.json
	./freeotp_to_andotp.py freeotp-backup.json |tee andotp_backup.json

