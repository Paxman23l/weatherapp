FROM raspbian/stretch
FROM python:3

ADD weather.py /
ADD requirements.txt /

RUN pip install -Ur requirements.txt

CMD ["python3", "./weather.py"]