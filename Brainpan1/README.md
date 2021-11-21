# Tools

# Knowledge

# Walkthrough
Scan with nmap for famous ports (```nmap -v -sV $TARGET_IP | tee nmap_result_famous_port```) 
```
Starting Nmap 7.91 ( https://nmap.org ) at 2021-11-19 21:08 CST
NSE: Loaded 45 scripts for scanning.
Initiating Ping Scan at 21:08
Scanning 10.10.173.1 [2 ports]
Completed Ping Scan at 21:08, 0.19s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 21:08
Completed Parallel DNS resolution of 1 host. at 21:08, 0.01s elapsed
Initiating Connect Scan at 21:08
Scanning 10.10.173.1 [1000 ports]
Discovered open port 10000/tcp on 10.10.173.1
Discovered open port 9999/tcp on 10.10.173.1
Completed Connect Scan at 21:08, 15.45s elapsed (1000 total ports)
Initiating Service scan at 21:08
Scanning 2 services on 10.10.173.1
Completed Service scan at 21:08, 17.41s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.173.1.
Initiating NSE at 21:08
Completed NSE at 21:09, 30.20s elapsed
Initiating NSE at 21:09
Completed NSE at 21:09, 0.82s elapsed
Nmap scan report for 10.10.173.1
Host is up (0.19s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE VERSION
9999/tcp  open  abyss?
10000/tcp open  http    SimpleHTTPServer 0.6 (Python 2.7.3)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.91%I=7%D=11/19%Time=619866BA%P=x86_64-pc-linux-gnu%r(N
SF:ULL,298,"_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\n_\|_\|_\|\x20\x20\x20\x20_\|\x20\x20_\|_\|\x20\x20\x20\x20_\|_\|_\
SF:|\x20\x20\x20\x20\x20\x20_\|_\|_\|\x20\x20\x20\x20_\|_\|_\|\x20\x20\x20
SF:\x20\x20\x20_\|_\|_\|\x20\x20_\|_\|_\|\x20\x20\n_\|\x20\x20\x20\x20_\|\
SF:x20\x20_\|_\|\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\
SF:x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\
SF:x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\n_\|\x20\x20\x20\x20_\
SF:|\x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20_\|\x20\
SF:x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\
SF:x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\n_\|_\|_\|\x20\
SF:x20\x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\|_\|_\|\x20\x20
SF:_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|_\|_\|\x20\x20\x20\x20\x20\
SF:x20_\|_\|_\|\x20\x20_\|\x20\x20\x20\x20_\|\n\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20_\|\n\n\[________________________\x20WELCOME\x20TO\x20BRAINPAN\
SF:x20_________________________\]\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20ENTER\
SF:x20THE\x20PASSWORD\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\n
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20>>\x20");

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 64.34 seconds
```

Gobuster a port 10000 (```gobuster dir -u http://$TARGET_IP:10000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x .txt,.md,.py,.out | tee gobuster_on_10000```)
```
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.173.1:10000
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,md,py,out
[+] Timeout:                 10s
===============================================================
2021/11/19 21:19:00 Starting gobuster in directory enumeration mode
===============================================================
/bin                  (Status: 301) [Size: 0] [--> /bin/]
```

Then, I found brainpan.exe in a directory named bin. (http://$TARGET_IP:10000/bin)

After analyzing brainpan.exe, I could get reverse shell to remote host.  
It seemed brainpan.exe was a wine program working on linux.  
Recreating an exploit script (exploit_linux.py), I could get a reverse shell to linux host.  
Running ```sudo -l``` told me that I could run ```/home/anansi/bin/anansi_util``` with privileged right.  
Seemingly anansi_util utilizes ```man``` command, which means I could run ```sudo man``` without password.  
Checking GTFOBins for privilege escalation from ```sudo man```, I could get root privilege.  