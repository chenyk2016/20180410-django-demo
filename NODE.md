# [编写你的第一个Django应用](https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/#write-your-first-view)

# 安装
~~~python
    # 安装django
    pip install django
    # 开启简易服务器
    python manage.py runserver
    # 创建一个应用
    python manage.py startapp polls
    # 通过以下命令打开 Python 命令行：
    python manage.py shell
    # 输出Django源码位置
    python -c "import django; print(django.__path__)"
    # 升级pip
    python -m pip install --upgrade pip
    # 卸载
    pip uninstall packageName


    # 在数据库中创建一些表
    # Python 内置 SQLite，所以你无需安装额外东西来使用它。
    python manage.py migrate
    # 创建模型
    python manage.py makemigrations polls
    # 查看数据迁移文件
    python manage.py sqlmigrate polls 0001
    # 迁移数据文件
    python manage.py migrate


~~~


# sqlite3
1. 开发工具 sqliteexpert：[下载地址](http://www.sqliteexpert.com/download.html)


# 模型
改变模型需要这三步
1.编辑 __models.py__ 文件，改变模型。
2.运行 __python manage.py makemigrations__ 为模型的改变生成迁移文件。
3.运行 __python manage.py migrate__ 来应用数据库迁移。

# 创建管理员账号
~~~python
    # python manage.py createsuperuser
~~~


# 配置
1. 配置语言
    ~~~python
        # zh-hans[中文] en-us[英文]
        LANGUAGE_CODE = 'zh-hans'
    ~~~

# 数据
1. 数据时提交竞争条件
    ~~~python
    运用 F
    from django.db.models import F
    ~~~


# python 
## 命令行
    输出
    print("===================hello world!")


# 打包应用``setuptools``
    ~~~cli
    pip install setuptools
    # 安装打包后的应用
    pip install --user django-polls/dist/django-polls-0.1.tar.gz
    ~~~

