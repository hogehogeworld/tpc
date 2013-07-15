from optparse import OptParseError,OptionParser
from scapy.all import *

usage = "%usage:%prog [option]"
parse = OptionParser(usage,version="Version:0.1")

def checker(option,opt_str,value,parser):
    if os.path.isfile(value):
        parser.values._file = value
    else:
        print "The file doesn't exist"

parse.add_option(
        '-f','--file',
        action='callback',
        callback = checker,
        type = 'string',
        dest = '_file',
        metavar = 'FILE',
        help = '<Pakcet_File>.pcap \t\t\tMUST'
        )

(options,args) = parse.parse_args()


try:
    _file = rdpcap(options._file)
except TypeError:
    print "Try:python pkc_raw.py -help"
    exit()

for i,j in enumerate(_file):
    _str = j.sprintf("%Raw.load%")
    print "{0}:\t{1}".format(i,_str) if _str != "??" else "{0}:\tNone".format(i)
