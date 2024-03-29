#!/usr/bin/python3
""" Load, add, save """

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    mylist = load_from_json_file(filename)
except:
    save_to_json_file([], filename)

mylist = load_from_json_file(filename)

for i in range(len(sys.argv)):
    if i > 0:
        mylist.append(sys.argv[i])

save_to_json_file(mylist, filename)
