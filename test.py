import http.client
import json


conn = http.client.HTTPSConnection("facebook-reel-and-video-downloader.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "9401f3099dmsh183323edbeb4857p1ca1e2jsn8f4e317df8cd",
    'X-RapidAPI-Host': "facebook-reel-and-video-downloader.p.rapidapi.com"
}

conn.request("GET", "/app/main.php?url=https://www.facebook.com/share/v/xqVtK9PjnPyhphCh/?mibextid=oFDknk", headers=headers)

res = conn.getresponse()
data = res.read()


my_string = data.decode('utf-8')
datas = json.loads(my_string)

praser_value = datas["links"]

print(praser_value)






# json_data = b'{"success":true,"praser":1}'

# # Parse the JSON data into a Python dictionary
# data_dict = json.loads(json_data)

# # Access the values in the dictionary
# success = data_dict['success']
# parser = data_dict['praser']

# print("Success:", success)
# print("Parser:", parser)