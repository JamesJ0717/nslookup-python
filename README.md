# nslookup-python
A simple python "script" to get some DNS information for a provided domain.

## Usage
From the command line, type `./nslookup.py [option] url`. It's as simple as that. 

### Options
Currently, there are three options: '-h', '-c', and '-a'. '-h' lists the help information. '-c' searches the more common DNS records like A, AAAA, ALIAS, CNAME, NS, PTR, SOA, SRV, and TXT. '-a' searches all of the DNS records for the given domain.
