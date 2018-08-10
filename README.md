# rest_backend

## 后台api接口模板

## 基础依赖

- python3.6+

- django2.1

## 其他依赖

- Django==2.1
- django-cors-headers==2.2.0
- django-debug-toolbar==1.9.1
- django-rest-swagger==2.1.2
- djangorestframework==3.8.2
- djangorestframework-jwt==1.11.0
- Pillow==5.1.0

## 初始化

```
git clone http://https://github.com/wuyue92tree/rest_backend.git

cd rest_backend

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

## 启动

浏览器访问： http://127.0.0.1:8000/api/docs/


## docker部署上线

```
git clone http://https://github.com/wuyue92tree/rest_backend.git

cd rest_backend

docker-compose up
```


## FAQ

[说明文档](http://wuyue92tree.antio.top/opensource/rest_backend.html#FAQ)
