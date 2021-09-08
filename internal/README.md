nmap result(./nmap_result)
	command : nmap -v -sV -p1-65535 $TARGET_IP | tee nmap_result

	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))


	
gobuster result(./gobuster_on_80
	command : gobuster dir -u http://$TARGET_IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .txt | tee gobuster_on_80

	/blog                 (Status: 301) [Size: 311] [--> http://10.10.88.179/blog/]
	/wordpress            (Status: 301) [Size: 316] [--> http://10.10.88.179/wordpress/]
	/javascript           (Status: 301) [Size: 317] [--> http://10.10.88.179/javascript/]
	/phpmyadmin           (Status: 301) [Size: 317] [--> http://10.10.88.179/phpmyadmin/]
	
