# 第三方app翻译

### settings.py中添加LOCALE_PATHS，不添加makemessages无法工作

```
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# mkdir [BASE_DIR]/locale
```


### 创建待翻译第三方app软连接到项目目录

```
ln -s ~/.virtualenvs/<virtyalenv>/lib/python3.4/site-packages/<app> ./
```

### 生成`.po`文件

```
./manage.py makemessages -s -l zh
```

### 创建第三方app翻译文件存放目录，并将生成的locale文件夹转移到存放目录

```$xslt
mkdir third_party_app_trans/<app>

cp -r <app>/locale third_party_app_trans/<app>/

rm <app>

```

### 将第三方app翻译文件路径加入到settings.py中

```$xslt
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'third_party_app_trans/<app>/locale'),
)
```

### 修改并编译

```$xslt
vi third_party_app_trans/<app>/locale/zh/django.po

./manage.py compilemessages
```