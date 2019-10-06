FROM arm32v7/python:2.7.16-buster

ADD weather.py /
ADD requirements.txt /

# Add sudoer
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker
RUN apt-get update
RUN apt-get install sense-hat
# RUN apt-get upgrade
# RUN apt-get install python2.7 python-pip python-dev libatlas-base-dev python-rtimulib
RUN pip install -r requirements.txt

CMD ["python", "./weather.py"]