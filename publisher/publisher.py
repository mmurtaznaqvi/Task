import rpyc
from scapy.all import *
from rpyc.utils.server import ThreadedServer

class PktGeneration(rpyc.Service):
    def exposed_send_pkt(self, ip):
        pkt = Ether()/IP(src=ip,dst="10.0.0.1")/UDP()/"Hello World"
        sendp(pkt, iface="ens8")
        
    def exposed_send_pkts(self, ip, pktcount):
        pkt = Ether()/IP(src=ip,dst="10.0.0.1")/UDP()/"Hello World"
        sendp(pkt, iface="ens8", count=pktcount)

if __name__ == "__main__":
    server = ThreadedServer(PktGeneration, port = 8081)
    server.start()