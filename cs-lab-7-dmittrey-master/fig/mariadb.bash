dmitry@dmitry-Surface-Pro-6:~$ sudo systemctl status mariadb
[sudo] пароль для dmitry:
🟢mariadb.service - MariaDB 10.5.6 database server
	Loaded: loaded (/lib/systemd/system/mariadb.service; enabled; vendor preset: enabled)
       Drop-In: /etc//systemd/system/mariadb.service.d
                └──migrated-from-my.cnf-settings.conf
        Active: active (running) since Sun 2020-10-25 23:20:29 MSK; 17min ago
          Docs: man:mariadb(8)
	        https://mariadb.com/kb/en/library/systemd/
      Main PID: 9489 (mariadbd)
        Status: "Talking your SQL requests now..."
         Tasks: 9 (limit: 9392)
        Memory: 75.0M
	CGroup: /system.slice/mariadb.service
	        └──9489 /usr/sbin/mariadbd

окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: Processing databases
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: information_schema
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: mysql
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: performance_schema
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: Phase 6/7: Checking and upgrading 
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: Processing databases
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: information_schema
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: performance_schema
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: Phase 7/7: Running 'FLUSH PRIVATE'
окт 25 23:20:31 dmitry-Surface-Pro-6 /etc/mysql/debian-start[9511]: OK