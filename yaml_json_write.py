#!/usr/bin/env python

'''
Creates a list that includeds a dictonary. Then writes the list to two files.
One file is in YAML formate, the other file is in JSON format.

'''

import yaml
import json


def main():

    yaml_file = 'test.yml'
    json_file = 'test.json'

    test_dict = {
        'vendor': 'fortigate',
        'mask': '255.255.255.0',
        'model': '800d',
        'ip_addr': '192.168.168.1'
    }

    test_list = [
        'something', 
        'stuff', 
        '1',
        '5', 
        test_dict,
        'string after dict',
        'last string'
    ]


    with open(yaml_file, "w") as f:
        f.write(yaml.dump(test_list, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(test_list, f)

if __name__ == "__main__":
   main()
