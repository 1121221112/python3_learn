FROM python:3.8.6
ENV LANG C.UTF-8

COPY ../api/requirments.txt /opt/flask/requirments.txt
WORKDIR /opt/flask

RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
   pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ && \
   pip3 install -r requirments.txt -i https://mirrors.aliyun.com/pypi/simple/

ENTRYPOINT ["bash", "-c", "python3 src/run.py"]