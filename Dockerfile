FROM balenalib/raspberrypi3-python:3.5.7-stretch-run

## COPY ALL REQUIRED APP FILES
#ADD requirements.txt /

## INSTALL UPDATES AND REQUIRED PACKAGES
RUN apt-get update && apt-get -y upgrade && \
	apt-get install -y --no-install-recommends libc-bin qt4-default libopenjp2-7 libssl-dev libffi-dev build-essential zlib1g-dev libjpeg-dev git wget

#RUN apt-get install -y --no-install-recommends build-essential
#RUN apt-get install -y --no-install-recommends libpng12-0 zlib1g-dev
#RUN apt-get install -y --no-install-recommends libjpeg-dev libopenjp2-7

## PIP UPGRADE AND INSTALL
RUN pip3 install --upgrade pip
#RUN CFLAGS=-std=c99 pip install numpy
RUN pip3 install numpy
## COPY ALL REQUIRED APP FILES
ADD requirements.txt /
RUN pip3 install -r requirements.txt

#RUN apt-get install -y git
#RUN apt-get install --reinstall ca-certificates
#RUN apt-get install --no-install-recommends wget

#RUN mkdir /usr/local/share/ca-certificates/cacert.org
#RUN wget -P /usr/local/share/ca-certificates/cacert.org http://www.cacert.org/certs/root.crt http://www.cacert.org/certs/class3.crt
#RUN update-ca-certificates
#RUN git config --global http.sslCAinfo /etc/ssl/certs/ca-certificates.crt

## INSTALL REQUIRED RTIMULIB
RUN git clone https://github.com/RPi-Distro/RTIMULib
WORKDIR RTIMULib/Linux/python
RUN python3.5 setup.py build && python3.5 setup.py install

## CLEANUP
WORKDIR /
RUN rm -r RTIMULib/ && rm requirements.txt
RUN apt-get remove -y git wget python3-pip && apt-get remove --purge x11-common && apt-get -y autoremove && apt-get -y autoclean
#RUN pip3 uninstall numpy -y
ADD main.py weather.py /

CMD ["python3.5", "./main.py"]
