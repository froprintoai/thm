# Tools
* nmap for enum  
# Knowledge

# Walkthrough
## Enumeration
The nmap default TCP scan reveals only 3 ports.  
```nmap -v -Pn -p1-65535 $TARGET_IP | tee nmap_result```  
```
	PORT     STATE SERVICE
	21/tcp   open  ftp
	3389/tcp open  ms-wbt-server
	9999/tcp open  abyss
```  
I accessed a ftp port using ftp command.
```ftp -v $TARGET_IP 21```  
I could use the default credential. (Username: anonymous / Password: )  
Found interesting files in chatserver directory.  
```
	ftp> ls
	200 PORT command successful.
	125 Data connection already open; Transfer starting.
	08-29-19  10:26PM                43747 chatserver.exe
	08-29-19  10:27PM                30761 essfunc.dll
```  

Then, I connected to a port 9999 using netcat, and it seemingly is related to chatserver.exe.  

Note that you need to use binary command before downloading chatserver.exe and essfunc.dll.  
```
	ftp> cd chatserver
	250 CWD command successful.
	ftp> binary
	200 Type set to I.
	ftp> mget *
	mget chatserver.exe? y
	200 PORT command successful.
	150 Opening BINARY mode data connection.
	226 Transfer complete.
	43747 bytes received in 1.53 secs (27.8335 kB/s)
	mget essfunc.dll? y
	200 PORT command successful.
	125 Data connection already open; Transfer starting.
	226 Transfer complete.
	30761 bytes received in 1.23 secs (24.4719 kB/s)
```

Next, to exploit this chat program using buffer overflow, you need to run it on Immunity Debugger.  
I set up Windows 7(,XP) on virtualbox, ran the program on Immunity Debugger, and connected from the host Machine.  
I tested the program by entering a number of As.  
![alt text](./images/As.png?raw=true)  
![alt text](./images/registers.png?raw=true)  
