# django-vue-robots

#### 学习指南

创建项目：django-admin startproject demo
如果已经存在空项目，创建后，需要修改所有设计demo的地方。

启动指令：python manage.py runserver 0.0.0.0:8000

创建一个应用：python manage.py startapp autobots


在配置完后，启动项目后可以访问app
http://localhost:8000/autobots

数据库迁移。真的很方便
```python
# makemigrations app  创建要迁移的app数据库模型，显示0001_xxxx
python manage.py makemigrations autobots

# 检查sql对不对 需要app和创建的迁移模型id
python manage.py sqlmigrate autobots 0001

# 执行真正迁移，写入数据库
python manage.py migrate
```

django admin
1. 在app的admin里面配置，admin.site.register(Model)
2. 在settings.INSTALLED_APPS中添加app