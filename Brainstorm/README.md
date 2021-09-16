# Tools

# Knowledge

# Walkthrough
==Enumeration==
The nmap default TCP scan reveals only 3 ports.  
```nmap -v -Pn -p1-65535 $TARGET_IP | tee nmap_result```  
```
	PORT     STATE SERVICE
	21/tcp   open  ftp
	3389/tcp open  ms-wbt-server
	9999/tcp open  abyss
```
