import json
from datetime import datetime
from django.shortcuts import render
from django.views.generic.base import View,TemplateView
from django.http import HttpResponse
from dao.searchLibrary import SearchManager

class IndexView(TemplateView):
    template_name = 'search/index.html'

class AllLibraryListView(View):
    def __init__(self):
        self.sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')

    def get(self, request):
        self.basic_list = self.sm.getBasicInfo()
        status = Status().getStatus(self.sm, self.basic_list)
        for i in range(len(self.basic_list)):
            if self.basic_list[i]['name'] == status[i]['name']:
                self.basic_list[i]['status'] = status[i]['status']
        result = json.dumps(self.basic_list, ensure_ascii=False)
        self.sm.close()
        return HttpResponse(result, content_type="application/json")

class LibraryListView(View):
    def __init__(self):
        self.sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')

    def get(self, request, name):
        self.basic_list = self.sm.getBasicInfo(name=name)
        status = Status().getStatus(self.sm, self.basic_list)
        for i in range(len(self.basic_list)):
            if self.basic_list[i]['name'] == status[i]['name']:
                self.basic_list[i]['status'] = status[i]['status']
        result = json.dumps(self.basic_list, ensure_ascii=False)
        self.sm.close()
        return HttpResponse(result, content_type="application/json")

class Status:
    def __init__(self):
        self.cur = datetime.now()

    def getStatus(self, searchManager, libraryNames):
        result = []
        days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        # 현재 요일, 시각, 분
        for i in range(len(libraryNames)):
            data = searchManager.getOperateTime(libraryNames[i]['name'])
            # cur = datetime.now()
            curDay = self.cur.weekday()
            curHour = self.cur.hour
            curMinute = self.cur.minute

            closeDay = data['close_day'].replace(',',' ').split()
            if curDay < 5:
                open = list(map(int, data['every_open'].split(':')))
                close = list(map(int, data['every_close'].split(':')))
            elif curDay == 5:
                open = list(map(int, data['sat_open'].split(':')))
                close = list(map(int, data['sat_close'].split(':')))
            else:
                open = list(map(int, data['holiday_open'].split(':')))
                close = list(map(int, data['holiday_close'].split(':')))

            # 휴관일
            if days[curDay] in closeDay:
                result.append({'name':libraryNames[i]['name'], 'status':'close'})
                continue

            # 오픈 전
            if open[0] > curHour or (open[0]==curHour and open[1]>curMinute):
                result.append({'name':libraryNames[i]['name'], 'status':'close'})
                continue

            # 운영 종료
            if close[0] < curHour or (close[0]==curHour and close[1]<curHour):
                result.append({'name':libraryNames[i]['name'], 'status': 'close'})
                continue

            result.append({'name':libraryNames[i]['name'], 'status':'open'})
        return result

class LibraryDetailView(View):
    def get(self, request, name):
        sm = SearchManager('localhost', 'ssacuser', 'ssac123!@#', 'libweb')
        details = sm.getDetailedInfo(name)
        sm.close()
        context = {'result' : details}
        return render(request, 'search/detail.html', context)
        # return HttpResponse(result, content_type="application/json")