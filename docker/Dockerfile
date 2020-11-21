FROM python:3

USER root

RUN apt-get update
RUN apt-get install -y vim less
RUN apt-get install -y zsh less
RUN apt-get install -y fish less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pep8
RUN pip install autopep8
RUN pip install coverage

# GCPのSDKをインストール
RUN pip install --upgrade google-cloud-storage

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

EXPOSE 8000
CMD ["bash"]

#FROM python:3.8-alpine
#
## author
#MAINTAINER  a1008u
#
##WORKDIR /app
##COPY ./python/ /app
##CMD ["python", "-m","http.server","80"]
