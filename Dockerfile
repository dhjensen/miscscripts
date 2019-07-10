# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7.4-alpine3.9

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=mailtood Version=0.0.1
EXPOSE 3000

ENV user="null" \
    password="null"

WORKDIR /app
COPY mailtood.py /app

#CMD ["python3", "mailtood.py", "-u", "${user}", "-p", "${password}"]
CMD python3 mailtood.py -u $user -p $password