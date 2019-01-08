from django.conf.urls import url
from . import views


app_name = 'weather'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^baoshan/(\w+)$', views.baoshan, name='baoshan'),
    url(r'^changning/(\w+)$', views.changning, name='changning'),
    url(r'^chongming/(\w+)$', views.chongming, name='chongming'),
    url(r'^fengxian/(\w+)$', views.fengxian, name='fengxian'),
    url(r'^hongkou/(\w+)$', views.hongkou, name='hongkou'),
    url(r'^huangpu/(\w+)$', views.huangpu, name='huangpu'),
    url(r'^jiading/(\w+)$', views.jiading, name='jiading'),
    url(r'^jinshan/(\w+)$', views.jinshan, name='jinshan'),
    url(r'^jinan/(\w+)$', views.jinan, name='jinan'),
    url(r'^minghang/(\w+)$', views.minghang, name='minghang'),
    url(r'^pudong/(\w+)$', views.pudong, name='pudong'),
    url(r'^nanhui/(\w+)$', views.nanhui, name='nanhui'),
    url(r'^qingpu/(\w+)$', views.qingpu, name='qingpu'),
    url(r'^songjiang/(\w+)$', views.songjiang, name='songjiang'),
    url(r'^xuhui/(\w+)$', views.xuhui, name='xuhui'),
    url(r'^yangpu/(\w+)$', views.yangpu, name='yangpu'),

]