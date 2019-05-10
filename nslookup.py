import subprocess, sys
types = ["A", "NS", "TXT", "CNAME", "AAAA", "MX"]
for type in types:
    command = "nslookup -type=" + type + " " + sys.argv[1]
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(type)
    if(error):
        print(error)
    print(output.decode("utf=8"))
