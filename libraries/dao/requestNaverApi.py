import requests
import json

class NaverApi():
    def __init__(self):
        self.client_id = "FJdRxqYzNHLO_kOdHfIl"
        self.client_secret = "n4iKxIRR5A"
        self.headers = {
            "X-Naver-Client-Id": self.client_id,
            "X-Naver-Client-Secret": self.client_secret
        }
        self.requestType = ['webkr', 'blog', 'news', 'book', 'local', 'kin', 'image']

    def searchWebKr(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[0] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result

    def searchBlog(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[1] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result

    def searchNews(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[2] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result

    def searchBook(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[3] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result

    def searchLocal(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[4] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result

    def searchKin(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[5] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result

    def searchImage(self, keyword):
        url = "https://openapi.naver.com/v1/search/" + self.requestType[6] + "?query=" + keyword
        r = requests.get(url, headers=self.headers)
        result = json.loads(r.text)
        return result
