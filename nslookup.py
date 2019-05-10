#! /usr/bin/env python3

import subprocess
import sys

if(sys.argv[1] == '-h'):
    print("-c, --common    Search the most common DNS records")
    print("-a, --all       Search all of the DNS records")
    exit()

if(sys.argv[1] == '-c' or sys.argv[1] == '--common'):
    types = ["A", "NS", "TXT", "CNAME", "AAAA", "MX", "ALIAS", "PTR", "SRV"]
    url = sys.argv[2]
elif(sys.argv[1] == '-a' or sys.argv[1] == '--all'):
    types = ["A", "AAAA", "AFSDB", "ALIAS", "ATMA", "CAA", "CERT", "CNAME", "DHCID", "DNAME", "DNSKEY", "DS", "HINFO", "ISDN", "LOC",
             "MB, MG, MINFO, MR", "MX", "NAPTR", "NS", "NSAP", "NSEC", "NSEC3", "NSEC3PARAM", "PTR", "RP", "RRSIG", "RT", "SOA", "SRV", "TLSA", "TXT", "X25"]
    url = sys.argv[2]
else:
    types = ["A", "NS", "CNAME"]
    url = sys.argv[1]
for type in types:
    command = "nslookup -type=" + type + " " + url
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(type)
    if(error):
        print(error)
    print(output.decode("utf=8"))
