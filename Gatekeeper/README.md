# Tools

# Knowledge

# Walkthrough
Scan with nmap  
```
	PORT      STATE    SERVICE            VERSION
	135/tcp   open     msrpc              Microsoft Windows RPC
	139/tcp   open     netbios-ssn        Microsoft Windows netbios-ssn
	445/tcp   open     microsoft-ds       Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
	3389/tcp  open     ssl/ms-wbt-server?
	6609/tcp  filtered unknown
	7740/tcp  filtered unknown
	10179/tcp filtered unknown
	11951/tcp filtered unknown
	22896/tcp filtered unknown
	31337/tcp open     Elite?
	32634/tcp filtered unknown
	34894/tcp filtered unknown
	49152/tcp open     msrpc              Microsoft Windows RPC
	49153/tcp open     msrpc              Microsoft Windows RPC
	49154/tcp open     msrpc              Microsoft Windows RPC
	49155/tcp open     msrpc              Microsoft Windows RPC
	49161/tcp open     msrpc              Microsoft Windows RPC
	49165/tcp open     msrpc              Microsoft Windows RPC
	50140/tcp filtered unknown
	59992/tcp filtered unknown
	65372/tcp filtered unknown
```

nc to 31337 (```nc $TARGET_IP 31337```)  
```
	hello
	Hello hello!!!
	hacker
	Hello hacker!!!
	help
	Hello help!!!
	h
	Hello h!!!
```
Seemingly an echo server is running on this port.  
Scan smb shares (```nmap -script=smb-enum-shares $TARGET_IP | tee nmap_smb_result```)
```
	Host script results:
	| smb-enum-shares: 
	|   account_used: guest
	|   \\10.10.40.122\ADMIN$: 
	|     Type: STYPE_DISKTREE_HIDDEN
	|     Comment: Remote Admin
	|     Anonymous access: <none>
	|     Current user access: <none>
	|   \\10.10.40.122\C$: 
	|     Type: STYPE_DISKTREE_HIDDEN
	|     Comment: Default share
	|     Anonymous access: <none>
	|     Current user access: <none>
	|   \\10.10.40.122\IPC$: 
	|     Type: STYPE_IPC_HIDDEN
	|     Comment: Remote IPC
	|     Anonymous access: READ
	|     Current user access: READ/WRITE
	|   \\10.10.40.122\Users: 
	|     Type: STYPE_DISKTREE
	|     Comment: 
	|     Anonymous access: <none>
	|_    Current user access: READ
```

Accessed to Users using smblient(```smbclient //$TARGET_IP/Users -p 445 ```), then I found gatekeeper.exe in Share folder.  
Set up Windows 7 32bit on virtual machine, ran Immunity Debugger on gatekeeper.  
It turned out that gatekeeper.exe is the service run on port 31337.  
