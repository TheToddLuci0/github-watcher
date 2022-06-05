FROM ubuntu:latest

LABEL org.opencontainers.image.authors="TheToddLuci0"
ENV GITHUB_TOKEN="CHANGEME"
CMD sed -i "s/CHANGEME/$GITHUB_TOKEN/" /etc/cron.d/hello-cron &&  cron && tail -f /var/log/cron.log

ADD crontab /etc/cron.d/hello-cron

RUN DEBIAN_FRONTEND=noninteractive apt-get update ;\
    DEBIAN_FRONTEND=noninteractive apt-get -y install cron python3 python3-pip;\ 
    rm -rf /var/lib/apt/lists/* ;\
    chmod 0644 /etc/cron.d/hello-cron ;\
    touch /var/log/cron.log 

COPY ./*.py /opt/
COPY ./repos.json /opt/
COPY requirements.txt /opt/
RUN pip install -r /opt/requirements.txt