import requests


i=3
for i in range(10):
    a = requests.get("https://dog.ceo/api/breeds/image/random").json()
    print(a['message'].split('/')[4])

    print(a['message'])

    file= open('readme.md','a')
    file.write(f"\n|{i}|{a['message'].split('/')[4]}|![pic]({a['message']})|")
    i+=1
file.close()