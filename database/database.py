from scapy.all import *

blacklist_file = open("blacklist_ip_list.txt", "r")
f = open('count_ip.txt','r')
filedata = f.read()

def extract_ip(pkt):
    global filedata
    if IP in pkt:
        ip_src=pkt[IP].src   
        for line in blacklist_file:
            if ip_src in line: 
                spt = filedata.split("\n")
                f.seek(0)
                for l in spt:
                    if ip_src in l:
                        l = l.rstrip()
                        c_spt = l.split()
                        count = c_spt[1]
                        re = int(count) + 1
                        repstr = c_spt[0] + " " + str(re)
                        filedata = filedata.replace(l,repstr)
                f.seek(0)
                write_file = open("count_ip.txt", "w")
                write_file.write(filedata)       
        blacklist_file.seek(0)

sniff(filter="ip",prn=extract_ip, store=0, iface="ens8")