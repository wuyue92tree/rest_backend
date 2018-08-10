FROM python:3.6.4
MAINTAINER wuyue92tree@163.com

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && mkdir -p /data/src

COPY ./requirements.txt /data/src
COPY ./pip.conf /root/.pip/pip.conf
COPY ./manage.py /data/src

WORKDIR /data/src

RUN pip install -r requirements.txt \
    && pip install https://github.com/darklow/django-suit/tarball/v2

EXPOSE 3031

CMD uwsgi uwsgi.ini