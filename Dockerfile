FROM brunneis/python:3.8.3-ubuntu-20.04

WORKDIR ./src/app/

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip3 install pandas flask torch xgboost google-cloud-storage

RUN python3 app.py