FROM gcr.io/google.com/cloudsdktool/cloud-sdk

WORKDIR ./src/app/

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip3 install pandas flask torch xgboost google-cloud-storage

CMD ["python3" "app.py"]
