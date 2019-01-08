from django.shortcuts import render
from django.http import HttpResponse
from .models import Weather


def index(request):
    return render(request, 'weather/index.html')


def baoshan(request, year):
    print('---1---')
    area = 'baoshan'
    date = Weather.objects.filter(area='baoshan').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/baoshan.html', locals())

def changning(request,year):
    print('---1---')
    date = Weather.objects.filter(area='changningqu').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/changning.html', locals())


def chongming(request,year):
    print('---1---')
    date = Weather.objects.filter(area='chongming').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/chongming.html', locals())

def fengxian(request,year):
    print('---1---')
    date = Weather.objects.filter(area='fengxian').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/fengxian.html', locals())

def hongkou(request,year):
    print('---1---')
    date = Weather.objects.filter(area='hongkou1').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/hongkou.html', locals())

def huangpu(request,year):
    print('---1---')
    date = Weather.objects.filter(area='huangpu1').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/huangpu.html', locals())

def jiading(request,year):
    print('---1---')
    date = Weather.objects.filter(area='jiading').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/jiading.html', locals())

def jinshan(request,year):
    print('---1---')
    date = Weather.objects.filter(area='jinshan').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/jinshan.html', locals())

def jinan(request,year):
    print('---1---')
    date = Weather.objects.filter(area='jinganqu').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/jinan.html', locals())

def minghang(request,year):
    print('---1---')
    date = Weather.objects.filter(area='minhang').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/minghang.html', locals())

def pudong(request,year):
    print('---1---')
    date = Weather.objects.filter(area='pudong').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/pudong.html', locals())

def nanhui(request,year):
    print('---1---')
    date = Weather.objects.filter(area='nanhui').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/nanhui.html', locals())

def qingpu(request,year):
    print('---1---')
    date = Weather.objects.filter(area='qingpu').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/qingpu.html', locals())

def songjiang(request,year):
    print('---1---')
    date = Weather.objects.filter(area='songjiang').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print('---2---')
    return render(request, 'weather/songjiang.html', locals())

def xuhui(request,year):
    print('---1---')
    date = Weather.objects.filter(area='xuhui').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print(len(y_low))
    print('---2---')
    return render(request, 'weather/xuhui.html', locals())


def yangpu(request,year):
    print('---1---')
    date = Weather.objects.filter(area='yangpuqu').filter(year=year)
    # print(date)
    x = [i.datetime for i in date]
    y_low = [int(i.t_low) for i in date]
    y_high = [int(i.t_high) for i in date]
    print(len(y_low))
    print('---2---')
    return render(request, 'weather/yangpu.html', locals())



