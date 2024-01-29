import json
from read import file_handling_opt
import os

# validation keys and values

class KeyData():
    def __init__(self):
        self.file_data = {}

    def set(self, key, data):
        try:
            self.file_data = file_handling_opt('r',"")
            # Check if key already exists
            if key in self.file_data:
                return 'Sorry, this key already exists'
            # Add the new key-value pair to the loaded data
            self.file_data[key] = data
            
            file_handling_opt('w',self.file_data)

            return 'Data added successfully'
            
        except Exception as e:
            print('Sorry, an error occurred: ', e)
    

    def update(self,key,new_data):
        try:
            self.file_data = file_handling_opt('r',"")
            # Check if key already exists
            if key in self.file_data:
               self.file_data[key] = new_data;
               file_handling_opt('w',self.file_data)
               return 'Data updated successfully'
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Sorry, an error occurred:', e)

    def remove(self,key):
        try:
            self.file_data = file_handling_opt('r',"")
            # Check if key already exists
            if key in self.file_data:
               del self.file_data[key];
               file_handling_opt('w',self.file_data)
               return 'Deleted key successfully'
            
            return 'Sorry this key are not exist'
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Sorry, an error occurred:', e)

    def get(self,key):
        try:
            self.file_data = file_handling_opt('r',"")
                # Check if key already exists
            if key in self.file_data:
                    return self.file_data[key]
        
            return 'Sorry this key are not exist'
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Sorry, an error occurred:', e)

    def hset(self,hash_name,key,data):
        try:

            self.file_data = file_handling_opt('r',"")

            # Check if key already exists
            if hash_name in self.file_data:
                return 'Sorry, this key already exists'

            ''' Data add from hash set format in multiple items are stored
               in one hash storage ; 
            '''
            self.file_data[hash_name] = {}
            self.file_data[hash_name][key] = data;

            file_handling_opt('w',self.file_data)

            return 'Data added successfully'
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Sorry, an error occurred:', e)

    def hget(self,hash_name,key):
        try:

            self.file_data = file_handling_opt('r',"")
             # Check if key already exists
            if hash_name in self.file_data:
                return self.file_data[hash_name][key]
            
            return 'Sorry this hashkey are not exist'
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Sorry, an error occurred:', e)


    def hgetall(self,hash_name):
        try:
            self.file_data = file_handling_opt('r',"")
            # Check if key already exists
            if hash_name in self.file_data:
                return self.file_data[hash_name]
            
            return 'Sorry this hashName are not exist'
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print('Sorry, an error occurred:', e)