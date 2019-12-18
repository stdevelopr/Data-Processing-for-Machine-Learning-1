From python:3

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD /data /data
WORKDIR /data

CMD [ "python", "./categorical_data.py" ]