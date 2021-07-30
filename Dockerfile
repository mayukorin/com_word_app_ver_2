FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /com-word-app2
WORKDIR /com-word-app2
COPY requirements.txt /com-word-app2/
RUN pip install -r requirements.txt
COPY . /com-word-app2/ 