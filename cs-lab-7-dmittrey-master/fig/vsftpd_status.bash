dmitry@dmitry-Surface-Pro-6:~$ sudo systemctl status vsftpd
[sudo] пароль для dmitry:
🟢vsftpd.service - vsftpd FTP server
	Loaded: loaded (/lib/systemd/system/vsftpd.service; enabled; vendor preset: enabled)
        Active: active (running) since Mon 2020-10-26 18:39:39 MSK; 2min 2s ago
      Main PID: 18137 (vsftpd)
         Tasks: 1 (limit: 9392)
        Memory: 660.0K
	CGroup: /system.slice/vsftpd.service
		└──18137 /usr/sbin/vsftpd /etc/vsftpd.conf

окт 26 14:11:52 dmitry-Surface-Pro-6 systemd[1]: Starting vsftpd FTP Server...
окт 26 14:11:52 dmitry-Surface-Pro-6 systemd[1]: Started vsftpd FTP Server.
