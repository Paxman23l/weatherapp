FROM balenalib/raspberrypi3-python:3.5.7-stretch-run

## INSTALL UPDATES AND REQUIRED PACKAGES
RUN apt-get update && apt-get -y upgrade && \
	apt-get install -y --no-install-recommends libc-bin qt4-default libopenjp2-7 libssl-dev libffi-dev build-essential zlib1g-dev libjpeg-dev git wget

## PIP UPGRADE AND INSTALL
RUN pip3 install --upgrade pip
RUN pip3 install numpy

## COPY REQUIREMENTS FILE AND INSTALL
ADD requirements.txt /
RUN pip3 install -r requirements.txt

## INSTALL REQUIRED RTIMULIB
RUN git clone https://github.com/RPi-Distro/RTIMULib
WORKDIR /RTIMULib/Linux/python
RUN python3.5 setup.py build && python3.5 setup.py install

## CLEANUP
WORKDIR /
RUN rm -r RTIMULib/ && rm requirements.txt
RUN apt-get remove -y git wget python3-pip && apt-get remove --purge x11-common && apt-get -y autoremove && apt-get -y autoclean

RUN pip3 install requests

# COPY PROGRAM FILES
COPY src/ /src/

CMD ["python3.5", "/src/main.py"]
