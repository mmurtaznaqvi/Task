import rpyc
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Director by giving IP address of machine runing publisher')
    parser.add_argument("-a", "--addr", help="IP Address of publisher", required=True)
    args = parser.parse_args()
    conn = None
    try:
        conn = rpyc.connect(args.addr, 8081)
    except BaseException as e:
        print e.message
    while True:
        val = input("Please Enter Command:  \n Enter 1 for Sending Single Packet \n Enter 2 for Sending multiple packets \n")
        if val == 1:
            srcip =  raw_input("Please Enter Source IP e.g. '172.30.1.1'\n")
            if conn:
                conn.root.send_pkt(str(srcip))
            else:
                print "Connection Not available"
        elif val == 2:
            srcip =  raw_input("Please Enter Source IP and Count e.g. '172.30.1.1 10'\n")
            srcip = srcip.split()
            if conn:
                conn.root.send_pkts(str(srcip[0]), int(srcip[1]))
            else:
                print "Connection Not available"
        else:
            print "Invalid Input"


