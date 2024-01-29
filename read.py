'''
  For reuseble data and file connection in this file for oprations such as
  read, write, etc;
  beacuse complexcity are maintain and fastest work with file in one time;
'''

import json
import os

def file_handling_opt(opration,new_writable_data):
    if opration == 'r':
       with open('./mystorage/storage.json', 'r') as file:
        loaded_data = json.load(file)
        return loaded_data

    elif opration == 'w':
        with open('./mystorage/storage.json', 'w') as file_write:
          json.dump(new_writable_data, file_write, indent=1)
     
