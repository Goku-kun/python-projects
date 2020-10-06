import json

file_token = json.load(open("./Installs.json","r"))
fopen = open("applist.txt","w")
temp = ""
for val in file_token:
      for x,y in val.items():
            for u,z in y.items():
                  if (isinstance(z,dict)):
                        if (z.get('title') is not None and temp != z.get('title')):
                              temp = z.get('title')
                              print(z.get('title'))
                              fopen.write(temp+"\n")
fopen.close()