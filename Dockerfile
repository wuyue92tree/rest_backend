FROM python:3.6.4
MAINTAINER wuyue92tree@163.com

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && mkdir -p /data/src \
    && mkdir -p /data/logs

COPY ./requirements.txt /data/src
COPY ./manage.py /data/src

WORKDIR /data/src

RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com\
    && pip install https://github.com/darklow/django-suit/tarball/v2 \
    && pip install git+https://github.com/Supervisor/supervisor

EXPOSE 3031
EXPOSE 5555
EXPOSE 9001

CMD supervisord -nc /etc/supervisor/supervisor.conf