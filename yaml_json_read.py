#!/usr/bin/env python

'''
Program that reads the yaml_json_write.py file and prints
out the data structure
'''

import yaml
import json

from pprint import pprint

def output_format(yj_list, yj_str):

    '''
    Makes the output easier to read
    '''

    print '\n\n'
    print '#' * 3
    print '#' * 3 + yj_str
    print '#' * 3
    pprint(yj_list)

def main():
    '''
    Reads the YAML and JSON files.
    Prints the files
    '''
    yaml_file = 'test.yml'
    json_file = 'test.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)

    with open(json_file) as f:
        json_list = json.load(f)

    output_format(yaml_list, ' YAML')
    output_format(json_list, ' JSON')
    print '\n'

if __name__ == "__main__":
    main()
