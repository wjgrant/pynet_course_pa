#!/usr/bin/env python
'''
Uses ciscoconfparse to parse 'cisco_ipsec.txt' config file

Script finds all crypto map entries ('crypto map CRYPTO') and
prints out all maps that are using pfs group2
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    finds all of the crypto map entires and prints all using pfs group2
    '''

    file_in = 'cisco_ipsec.txt'

    config_file = CiscoConfParse(file_in)
    crypto_maps = config_file.find_objects_w_child(parentspec=r'crypto map CRYPTO',
                                                  childspec=r'pfs group2')

    print "\nCrypto Maps using PFS group2:"
    for entry in crypto_maps:
        print " {0}".format(entry.text)
    print

if __name__ == "__main__":
    main()
