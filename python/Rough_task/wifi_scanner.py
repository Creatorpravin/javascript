import scapy.all as scapy 
  
request = scapy.ARP() 
    
request.pdst = '192.168.0.0/24'
broadcast = scapy.Ether() 
    
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    
request_broadcast = broadcast / request 
print(broadcast)
print(request)
print(request_broadcast)
clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0] 
for element in clients: 
    print(element[1].psrc + "      " + element[1].hwsrc) 

