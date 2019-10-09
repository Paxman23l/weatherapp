FROM balenalib/raspberrypi3:jessie-build


#ADD weather.py /
## COPY ALL REQUIRED APP FILES
ADD main.py weather.py requirements.txt /

## INSTALL UPDATES AND REQUIRED PACKAGES
RUN apt-get update && apt-get -y upgrade && apt-get install -y curl python-numpy python-pil dpkg apt-utils libc-bin libopenjp2-7 python3-pip qt4-default build-essential libssl-dev libffi-dev python3-dev
#RUN apt-get install -y libc-bin
#RUN apt-get install -y libopenjp2-7
#RUN apt-get install -y python3-pip
#RUN apt-get install -y qt4-default

## INSTALL PYTHON3.5
RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
RUN tar -xvf Python-3.5.2.tar.xz
WORKDIR Python-3.5.2
RUN ./configure
RUN make
RUN make altinstall
WORKDIR /

## PIP UPGRADE AND INSTALL
RUN pip3.5 install --upgrade pip
#RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
RUN CFLAGS=-std=c99 pip3.5 install numpy
RUN pip3.5 install -r requirements.txt

## INSTALL REQUIRED RTIMULIB
RUN git clone https://github.com/RPi-Distro/RTIMULib
WORKDIR RTIMULib/Linux/python
RUN python3.5 setup.py build && python3.5 setup.py install
#RUN python3.5 setup.py install

## CLEANUP
WORKDIR /
RUN rm -r RTIMULib/ && rm /Python-3.5.2.tar.xz
RUN apt-get -y autoremove && apt-get -y autoclean

#ADD main.py weather.py requirements.txt /
CMD ["python3.5", "./main.py"]
