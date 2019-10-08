#FROM arm32v7/python:3.5-stretch
FROM balenalib/raspberrypi3:jessie-build


ADD weather.py /
ADD requirements.txt /
RUN apt-get update && apt-get -y upgrade && apt-get install -y curl python-numpy python-pil dpkg apt-utils 
RUN apt-get install -y libc-bin
RUN apt-get install -y libopenjp2-7
RUN apt-get install -y python3-pip
#RUN apt-get install -y cmake
RUN apt-get install -y qt4-default
#RUN apt-get install -y git
#RUN git clone https://github.com/RPi-Distro/RTIMULib.git

#WORKDIR /RTIMULib/Linux

#RUN mkdir build
#WORKDIR build

#RUN cmake ..
#RUN make

#WORKDIR /
#WORKDIR /tmp

#RUN wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/librtimulib-dev_7.2.1-5_armhf.deb \
# && wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib//librtimulib-utils_7.2.1-5_armhf.deb \
# && wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/librtimulib7_7.2.1-5_armhf.deb \
# && wget https://archive.raspberrypi.org/debian/pool/main/r/rtimulib/python3-rtimulib_7.2.1-5_armhf.deb \
# && wget https://archive.raspberrypi.org/debian/pool/main/p/python-sense-hat/python3-sense-hat_2.2.0-1_armhf.deb

#RUN dpkg -i librtimulib-dev_7.2.1-5_armhf.deb librtimulib-utils_7.2.1-5_armhf.deb librtimulib7_7.2.1-5_armhf.deb python3-rtimulib_7.2.1-5_armhf.deb python3-sense-hat_2.2.0-1_armhf.deb

RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
RUN tar -xvf Python-3.5.2.tar.xz
WORKDIR Python-3.5.2
RUN ./configure
RUN make
RUN make altinstall
WORKDIR /

RUN pip3.5 install --upgrade pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
RUN CFLAGS=-std=c99 pip3.5 install numpy
RUN pip3.5 install -r requirements.txt
#RUN pip3 install rtimulib

RUN git clone https://github.com/RPi-Distro/RTIMULib
WORKDIR RTIMULib/Linux/python
RUN python3.5 setup.py build
RUN python3.5 setup.py install

WORKDIR /
ADD main.py /
CMD ["python3.5", "./main.py"]
