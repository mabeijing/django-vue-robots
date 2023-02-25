from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

"""
配置path(route, view, name, **kwargs)

route 是一个路由规则，就是一个正则表达式
view 试图函数
name 给试图函数起名字，为了在后面引用
kwargs 高级参数。。。
"""