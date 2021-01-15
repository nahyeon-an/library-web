import json
import pandas as pd
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from dao.searchLibrary import SearchManager


class HomeView(TemplateView):
    template_name = 'home.html'


class DataView(View):
    def get(self, request):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        result = sm.getAllData("name", "sido_nm", "gungu_nm", "address")
        df = pd.DataFrame(result)
        city_group = df.groupby('sido_nm').count()
        keys = ["sido_nm", "count"]
        res = []
        for index, row in city_group.iterrows():
            res.append({keys[0]: index, keys[1]: int(row['name'])})
        res = json.dumps(res, ensure_ascii=False)
        sm.close()
        return HttpResponse(res, content_type="application/json")


class SiDataView(View):
    def get(self, request):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        result = sm.getAllData("name", "sido_nm", "books")
        df = pd.DataFrame(result)
        city_sum = df.groupby('sido_nm').sum()
        keys = ["sido_nm", "books_count"]
        res = []
        for index, row in city_sum.iterrows():
            res.append({keys[0]: index, keys[1]: int(row['books'])})
        res = json.dumps(res, ensure_ascii=False)
        sm.close()
        return HttpResponse(res, content_type="application/json")


class GunDataView(View):
    def get(self, request, name):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        result = sm.getAllData("name", "sido_nm", "gungu_nm", "books")
        df = pd.DataFrame(result)
        gun_sum = df.groupby(['sido_nm', 'gungu_nm']).sum().reset_index()
        gun_sum = gun_sum.loc[ gun_sum['sido_nm'] == name ]
        keys = ["sido_nm", "gungu_nm", "books_count"]
        res = []
        for i in range(len(gun_sum)):
            res.append({keys[0]: gun_sum.iloc[i]['sido_nm'], \
                        keys[1]: gun_sum.iloc[i]['gungu_nm'], \
                        keys[2]: int(gun_sum.iloc[i]['books'])})
        res = json.dumps(res, ensure_ascii=False)
        sm.close()
        return HttpResponse(res, content_type="application/json")

