FROM arm32v7/python:3.7.4-buster

#FROM raspbian/stretch:041518

#FROM armhf/ubuntu

ADD weather.py /
ADD requirements.txt /

RUN apt-get update && apt-get -y upgrade && apt-get install -y curl python-numpy python-pil dpkg

WORKDIR /tmp

RUN wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/librtimulib-dev_7.2.1-5_armhf.deb \
 && wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib//librtimulib-utils_7.2.1-5_armhf.deb \
 && wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/librtimulib7_7.2.1-5_armhf.deb \
 && wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/python3-rtimulib_7.2.1-5_armhf.deb \
 && wget https://archive.raspberrypi.org/debian/pool/main/p/python-sense-hat/python3-sense-hat_2.2.0-1_armhf.deb

RUN dpkg -i librtimulib-dev_7.2.1-5_armhf.deb librtimulib-utils_7.2.1-5_armhf.deb librtimulib7_7.2.1-5_armhf.deb python3-rtimulib_7.2.1-5_armhf.deb python3-sense-hat_2.2.0-1_armhf.deb


#RUN apt-get -y install sense-hat python2.7 python-pip python-dev libatlas-base-dev
# RUN apt-get upgrade
# RUN sudo apt-get install python2.7 python-pip python-dev libatlas-base-dev python-rtimulib
RUN sudo pip3 install -r requirements.txt

CMD ["python3", "./weather.py"]
