from optparse import OptParseError,OptionParser

from scapy.all import *
#from sys import argv

usage = "usage:%prog [option]"

parse = OptionParser(usage,version='Vesion:2.0')

def checker(option,opt_str,value,parser):
    if os.path.isfile(value):
        parser.values.file = value
    else:
        print "The file doesn't exist"

parse.add_option(
        '-f','--file',
        action = 'callback',
        callback = checker,
        type = 'string',
        dest = 'file',
        metavar="FILE",
        help = '<PacketFile>.pcap'
        )

parse.add_option(
        '-l',
        dest = 's',
        type = 'choice',
        choices = ['I','E'],
        metavar = "LAYER",
        help = "Input 'I'(IPaddr) or 'E'(Etheraddr)"
        )


(options,args) = parse.parse_args()

"""if not args:
    parse.error('requires Keyword')
    exit()
"""

PACK = rdpcap(options.file)
s = options.s 


if "I" in s:
    IPLIST = [i.sprintf("%IP.dst%") for i in PACK]
    IPLIST2 = [i.sprintf("%IP.src%") for i in PACK]
else:
    IPLIST = [i.sprintf("%Ether.dst%") for i in PACK]
    IPLIST2 = [i.sprintf("%Ether.src%") for i in PACK]

#IPLIST = sorted(set(IPLIST),key=IPLIST.index)
#IPLIST2 = sorted(set(IPLIST),key=IPLIST2.index)

NEW=[]
NEW2=[]

for i in IPLIST:
    if i not in NEW: NEW.append(i)
    else: continue
for i in IPLIST2:
    if i not in NEW2: NEW2.append(i)
    else: continue
print "SRC:"
for j in NEW2: print "\t"+j
print "DST:"
for i in NEW: print "\t"+i
