dmitry@dmitry-Surface-Pro-6:~$ sudo ufw allow 20/tcp
[sudo] пароль для dmitry:
Правило обновлено
Правило обновлено (v6)
dmitry@dmitry-Surface-Pro-6:~$ sudo ufw allow 21/tcp
Правило обновлено
Правило обновлено (v6)
dmitry@dmitry-Surface-Pro-6:~$ sudo ufw status
Состояние: активен

В		Действие	 Из
-		- - - - -	- -
Apache            ALLOW           Anywhere
OpenSSH           ALLOW           Anywhere
20/tcp            ALLOW           Anywhere
21/tcp            ALLOW           Anywhere
Apache (v6)       ALLOW           Anywhere (v6)
OpenSSH (v6)      ALLOW           Anywhere (v6)
20/tcp (v6)       ALLOW           Anywhere (v6)
21/tcp (v6)       ALLOW           Anywhere (v6)