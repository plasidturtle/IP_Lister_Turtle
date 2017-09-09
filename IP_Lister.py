#pip install netaddr
from netaddr import IPNetwork

def convert_cidr(ip_address):
    for ip in IPNetwork(ip_address):
        print ('%s' % ip)

def convert_range(ip_address):
    range_split = ip_address.split('-')
    start_ip = range_split[0]
    ip_split = start_ip.split('.')
    end_ip = ip_split[0]+"."+ip_split[1]+"."+ip_split[2] + "."+range_split[1]
    #end_ip = ip_split2[0:3]+ip_split1[1]
    #print(ip_split_string)
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))

    return ip_range

def main():
    #ip_address = input("Give me Ip")
    ip_address = "192.168.1.1/24"
    if '/' in ip_address:
        convert_cidr(ip_address)
    elif '-' in ip_address:
        print("\n".join(convert_range(ip_address)))

main()