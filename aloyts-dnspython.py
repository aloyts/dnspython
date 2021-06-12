import dns.resolver  # from dnspython: http://www.dnspython.org/
import socket

#================================================
# Author:      Aloyts
# Create Date: 2018 Nov 04
# Description: Output domain's permitted IPs
#================================================

def ips(domain, rectype):

    strIP = ""
    myResolver = dns.resolver.Resolver()
    myAnswers = myResolver.query(domain, rectype)    
    
    for rdata in myAnswers: 
            strIP += str(rdata)
            
    print(domain)
    print("________________________________________")
    print("whole str:" +strIP)

    allArr = strIP.split(" ")
    
    print("KeyVal Loop:\n")
    
    for i in range (0, len(allArr)):
        
        keyVal = allArr[i].split(":") # split txt "ip4:" and the IP addr
        
        secVal = keyVal[len(keyVal)-1]
        
        if rectype == "txt":
            if keyVal[0] == "ip4":    # break down the IP into singles from potential ranges
                if secVal.find("/") > -1:
                    secVal = secVal[0:secVal.find("/")]
                
                fqdn = socket.getfqdn(secVal)
                
                print(str(i) + ":" + keyVal[0] + "=" + keyVal[len(keyVal)-1] + 
                      "; IP:" + secVal + "; FQDN:" + fqdn + "\n")
            elif keyVal[0] == "ip6":
                print(str(i) + ":" + keyVal[0] + "=" + allArr[i] + "\n")
            else:
                print(str(i) + ":" + keyVal[0] + "=" + keyVal[len(keyVal)-1] + "\n")
        else:
            print(str(i) + ":" + keyVal[0] + "=" + keyVal[len(keyVal)-1] + "\n")
    
    return

'usage below: (domain, txt rec)'
ips("aloyts.com", "txt")