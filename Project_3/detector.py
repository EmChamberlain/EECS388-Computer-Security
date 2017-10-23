import dpkt
import sys



def exists(ips, ip):
    for key in ips:
        if key == ip:
            return True
    return False

def main():
    f = open(sys.argv[1])
    pcap = dpkt.pcap.Reader(f)

    ips = {}

    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        syn_flag = (tcp.flags & dpkt.tcp.TH_SYN) != 0
        ack_flag = (tcp.flags & dpkt.tcp.TH_ACK) != 0
        if syn_flag and not ack_flag:
            if exists(ips, ip.src):
                ips[ip.src][0] += 1
            else:
                ips[ip.src] = (1, 0)
        if syn_flag and ack_flag:
            if exists(ips, ip.dst):
                ips[ip.dst][1] += 1
            else:
                ips[ip.dst] = (0, 1)

    suspect = []

    for ip in ips:
        syn_count = ips[ip][0]
        syn_ack_count = ips[ip][1]
        if syn_count >= 3*syn_ack_count:
            suspect.append(ip)



if __name__ == "__main__":
    main()


