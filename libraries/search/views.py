import json

from django.shortcuts import render
from django.views.generic.base import View,TemplateView
from django.http import HttpResponse
from dao.searchLibrary import SearchManager

class IndexView(TemplateView):
    template_name = 'search/index.html'

class AllLibraryListView(View):
    def get(self, request):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        basic_list = sm.getBasicInfo()
        result = json.dumps(basic_list, ensure_ascii=False)
        sm.close()
        return HttpResponse(result, content_type="application/json")

class LibraryListView(View):
    def get(self, request, name):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        basic_list = sm.getBasicInfo(name=name)
        result = json.dumps(basic_list, ensure_ascii=False)
        sm.close()
        return HttpResponse(result, content_type="application/json")

class DetailView(TemplateView):
    template_name = 'search/detail.html'

class LibraryDetailView(View):
    def get(self, request, name):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        details = sm.getDetailedInfo(name)
        result = json.dumps(details, ensure_ascii=False)
        sm.close()
        context = {'result' : details}
        return render(request, 'search/detail.html', context)
        # return HttpResponse(result, content_type="application/json")