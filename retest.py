import requests

url = 'https://api.thecatapi.com/v1/images/search'
catimgs = []
n = 0
res = eval(requests.get(url).text)[0]["url"][-3:]
while n < 20:
    res = eval(requests.get(url).text)[0]["url"]
    print(res)
    if "gif" in res[-4:]:
        print(3)
        n += 1
        catimgs.append(res)
print(catimgs)
