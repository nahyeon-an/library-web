# 네이버 검색 api 가 잘 동작하는지, 결과 확인
import requests
import json

# 웹문서, 블로그, 뉴스, 책, 지역, 지식인, 이미지
req = ['webkr', 'blog', 'news', 'book', 'local', 'kin', 'image']
client_id = "FJdRxqYzNHLO_kOdHfIl"
client_secret = "n4iKxIRR5A"
keyword = "파이썬"
url = "https://openapi.naver.com/v1/search/" + req[3] + "?query=" + keyword  # json 결과
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

r = requests.get(url, headers=headers)
result = json.loads(r.text)
items = result['items']

print(type(items))
print(len(items))
print(items[0])
