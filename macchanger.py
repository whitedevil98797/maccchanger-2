# new tecnique to change mac 


import subprocess

new_mac = input("enter your own mac : ")
interface = input("enter your interface name : ") #ex-wlan0 or eth0

subprocess.run(["ifconfig", interface,"down"]) 
subprocess.run(["ifconfig" , interface ,"hw", "ether", new_mac ])
subprocess.run(["ifconfig" , interface , "up"])

print("your mac is changed successfully") 




