# Import requests package
import requests
import json

# Assign URL to variable: url

url = "http://www.omdbapi.com/?apikey=72bc447a&t=AVatar"
# Package the request, send the request and catch the response: r
r = requests.get(url)

json_data = r.json() 

# Print the text of the response
for k in json_data.keys():
    print(k + ': ', json_data[k])
