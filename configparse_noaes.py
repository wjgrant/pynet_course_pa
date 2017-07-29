#!/usr/bin/env python
'''
Uses ciscoconfparse to parse 'cisco_ipsec.txt' config file

Script finds all crypto map entries ('crypto map CRYPTO') and
prints out all maps that are not using AES
'''

import re
from ciscoconfparse import CiscoConfParse

def main():
    '''
    finds all of the crypto map entires and prints all that are not using AES
    '''

    file_in = 'cisco_ipsec.txt'

    config_file = CiscoConfParse(file_in)
    crypto_maps = config_file.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                                  childspec=r'AES')

    print "\nCrypto maps not using AES:"
    for entry in crypto_maps:
        for child in entry.children:
            if 'transform' in child.text:
                match = re.search(r"set transform-set (.*)$", child.text)
                encryption = match.group(1)
        print " {0} >>> {1}".format(entry.text.strip(), encryption)
    print

if __name__ == "__main__":
    main()
