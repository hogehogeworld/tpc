from optparse import OptParseError,OptionParser

from scapy.all import *
#from sys import argv

usage = "usage:%prog [option]"
parse = OptionParser(usage,version='Vesion:2.3')

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
        help = '<PacketFile>.pcap \t\t\tMUST'
        )
(options,args) = parse.parse_args()
try:
    PACK = rdpcap(options.file)
except TypeError:
    print "Try:python same_ip.py -h"
    exit()


IP_ETHER_LIST ={}
IP_ETHER_LIST2 ={}
for i in PACK:
    IP_ETHER_LIST[i.sprintf("%IP.dst%")] = i.sprintf("%Ether.dst%")
    IP_ETHER_LIST2[i.sprintf("%IP.src%")] = i.sprintf("%Ether.src%")

print "SRC:"
for i in IP_ETHER_LIST2:
    if "??" in i:
        print "\t{0}\t\t\t:{1}".format(i,IP_ETHER_LIST2[i])
    else:
        print "\t{0}\t\t:{1}".format(i,IP_ETHER_LIST2[i])

print "DST:"
for j in IP_ETHER_LIST:
    if "??" in j:
        print "\t{0}\t\t\t:{1}".format(j,IP_ETHER_LIST[j])
    else:
        print "\t{0}\t\t:{1}".format(j,IP_ETHER_LIST[j])
