#!/usr/bin/env python
'''
Uses ciscoconfparse to parse 'cisco_ipsec.txt' config file

Script finds all crypto map entries ('crypto map CRYPTO') and
prints out all children of each crypto map
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    finds all of the crypto map entires and prints all children
    '''

    file_in = 'cisco_ipsec.txt'

    config_file = CiscoConfParse(file_in)
    crypto_maps = config_file.find_objects(r"^crypto map CRYPTO")

    for c_map in crypto_maps:
        print
        print c_map.text
        for child in c_map.children:
            print child.text
    print

if __name__ == "__main__":
    main()
