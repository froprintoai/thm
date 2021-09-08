nmap result(./nmap_result)  
	```nmap -v -sV -p1-65535 $TARGET_IP | tee nmap_result```

	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))


	
gobuster result(./gobuster_on_80)  
	```gobuster dir -u http://$TARGET_IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .txt | tee gobuster_on_80```

	/blog                 (Status: 301) [Size: 311] [--> http://10.10.88.179/blog/]
	/wordpress            (Status: 301) [Size: 316] [--> http://10.10.88.179/wordpress/]
	/javascript           (Status: 301) [Size: 317] [--> http://10.10.88.179/javascript/]
	/phpmyadmin           (Status: 301) [Size: 317] [--> http://10.10.88.179/phpmyadmin/]
	/phpmyadmin/index.php            (Status: 200) [Size: 10531]
	/phpmyadmin/templates            (Status: 403) [Size: 277]  
	/phpmyadmin/themes.php           (Status: 200) [Size: 10532]
	/phpmyadmin/themes               (Status: 301) [Size: 324] [--> http://10.10.88.179/phpmyadmin/themes/]
	/phpmyadmin/doc                  (Status: 301) [Size: 321] [--> http://10.10.88.179/phpmyadmin/doc/]   
	/phpmyadmin/license.php          (Status: 200) [Size: 10533]                                           
	/phpmyadmin/navigation.php       (Status: 200) [Size: 10536]                                           
	/phpmyadmin/js                   (Status: 301) [Size: 320] [--> http://10.10.88.179/phpmyadmin/js/]    
	/phpmyadmin/logout.php           (Status: 200) [Size: 10532]                                           
	/phpmyadmin/libraries            (Status: 403) [Size: 277]                                             
	/phpmyadmin/changelog.php        (Status: 200) [Size: 10535]                                           
	/phpmyadmin/url.php              (Status: 302) [Size: 0] [--> /phpmyadmin/]                            
	/phpmyadmin/export.php           (Status: 200) [Size: 10532]                                           
	/phpmyadmin/setup                (Status: 401) [Size: 459]                                             
	/phpmyadmin/sql.php              (Status: 200) [Size: 10529]                                           
	/phpmyadmin/sql                  (Status: 301) [Size: 321] [--> http://10.10.88.179/phpmyadmin/sql/]   
	/phpmyadmin/locale               (Status: 301) [Size: 324] [--> http://10.10.88.179/phpmyadmin/locale/]
	/phpmyadmin/import.php           (Status: 200) [Size: 10532] 
	
After examining /phpmyadmin, seemingly mysql is behind the site.  

SQLMap didn't find any parameter injectable.  




