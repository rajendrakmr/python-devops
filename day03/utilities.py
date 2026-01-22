import json

# read line file
def read_file(filename):
    with open(filename,"r") as file:
        return file.readlines()
    
# write json file
def write_json(filename,json_object):
    with open(filename,"+w") as file:
        json.dump(json_object,file)