# rest_backends

## 后台api接口模板

## 基础依赖

- python3.6+

- django2.0.4

## 其他依赖

- Django==2.0.4
- django-cors-headers==2.2.0
- django-debug-toolbar==1.9.1
- django-rest-swagger==2.1.2
- djangorestframework==3.8.2
- djangorestframework-jwt==1.11.0

## 初始化

```
git clone http://gogs.antio.top/wuyue/rest_backend.git

cd rest_backend

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

## 启动

浏览器访问： http://127.0.0.1:8000/api-docs/