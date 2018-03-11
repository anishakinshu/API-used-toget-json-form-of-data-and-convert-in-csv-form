import sys
import json
import csv
import requests

##
# Convert to string keeping encoding in mind...
##

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=b77f71821c1145148cb7880b60bd4ec3')

response=requests.get(url)
raw_data = json.loads(response.content)

def to_string(s):
    try:
        return str(s)
    except:
        #Change the encoding type if needed
        return s.encode('utf-8')

def reduce_item(key, value):
    global reduced_item
    
    #Reduction Condition 1
    if type(value) is list:
        i=0
        for sub_item in value:
            reduce_item(key+'_'+to_string(i), sub_item)
            i=i+1

    #Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key+'_'+to_string(sub_key), value[sub_key])
    
    #Base Condition
    else:
        reduced_item[to_string(key)] = to_string(value)


if __name__ == "__main__":
    
        #Reading arguments
       
        
        #fp = open(json_file_path, 'r')
        #json_value = fp.read()
        #raw_data = json.loads(json_value)
        node = sys.argv[1]
        csv_path = sys.argv[2]
        
        try:
            data_to_be_processed = raw_data[node]
        except:
            data_to_be_processed = raw_data

        processed_data = []
        header = []
        
        for item in data_to_be_processed:
            reduced_item = {}
            reduce_item(node, item)

            header += reduced_item.keys()

            processed_data.append(reduced_item)

        header = list(set(header))
        header.sort()

'''save the csv form of json data in file name csv_file'''

        with open('csv_file', 'w+') as f:
            writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in processed_data:
                writer.writerow(row)

print ("Just completed writing csv file with %d columns" % len(header))
