FROM wuyue/python3-app:with_nginx
MAINTAINER wuyue92tree@163.com

COPY . /data/src
COPY ./deploy.ini /etc/supervisor/conf.d/
COPY ./_product/nginx.conf /usr/local/nginx/conf/nginx.conf

RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com \
    && pip install https://github.com/darklow/django-suit/tarball/v2

RUN python manage.py collectstatic --noinput

WORKDIR /data/src

EXPOSE 5555
EXPOSE 9001
EXPOSE 80
