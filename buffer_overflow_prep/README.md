# Tools

# Knowledge

# Walkthrough
Here are the short description about the target host from Task1.  
* OS: Windows7(32-bit)
* Immunity Debugger and Putty are preinstalled
* Windows Firewall and Defender are disabled  

With oscp.exe running on the target host, I executed a fuzzing python script, which crashed after sending 2000 bytes.  
```python3 fuzzer.py```  
We could see the contents of the registers.  
![alt text](./images/fuzzer_registers_result.png?raw=true)
![alt text](./images/fuzzer_registers_diagram.png?raw=true)  

Then, I sent a cyclic pattern of 2400(2000+400) bytes.  
The contents of the registers are below.  
![alt text](./images/exploit_registers_result.png?raw=true)  
Using the python script(mona.py), I checked a cyclic pattern on memory stack.  
```!mona findmsp -distance 2400```  
![alt text](./images/mona_result.png?raw=true)  
![alt text](./images/mona_diagram.png?raw=true)  


