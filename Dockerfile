FROM balenalib/raspberrypi3:jessie-run
#-build

## COPY ALL REQUIRED APP FILES
ADD main.py weather.py requirements.txt /

## INSTALL UPDATES AND REQUIRED PACKAGES
RUN apt-get update && apt-get -y upgrade && apt-get install --no-install-recommends -y wget python-numpy python-pil libc-bin python3-pip build-essential python3-dev

RUN apt-get install -y --no-install-recommends libssl-dev

## INSTALL PYTHON3.5
RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
RUN tar -xvf Python-3.5.2.tar.xz
WORKDIR Python-3.5.2
RUN ./configure
RUN make
RUN make altinstall
WORKDIR /

#RUN apt-get install -y --no-install-recommends libssl-dev
## PIP UPGRADE AND INSTALL
RUN pip3.5 install --upgrade pip
RUN CFLAGS=-std=c99 pip3.5 install numpy
RUN apt-get install -y --no-install-recommends libjpeg-dev zlib1g-dev
RUN pip3.5 install -r requirements.txt

RUN apt-get install -y --no-install-recommends git

## INSTALL REQUIRED RTIMULIB
RUN git clone https://github.com/RPi-Distro/RTIMULib
WORKDIR RTIMULib/Linux/python
RUN python3.5 setup.py build && python3.5 setup.py install
#RUN python3.5 setup.py install

## CLEANUP
WORKDIR /
RUN rm -r RTIMULib/ && rm /Python-3.5.2.tar.xz
RUN apt-get remove -y wget git && rm -rf /var/lib/apt/lists* && apt-get clean && apt-get -y autoremove && apt-get -y autoclean

#ADD main.py weather.py requirements.txt /
CMD ["python3.5", "./main.py"]
