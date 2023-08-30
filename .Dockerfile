FROM python:3.7-alpine

#RUN install pip3

RUN pip3 install flask

WORKDIR /app

COPY flaskApp.py /app

COPY /template /app/template

#EXPOSE 5000

CMD ["python", "flaskApp.py"]
