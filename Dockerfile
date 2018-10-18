FROM python:alpine
#RUN apt update -y
#RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
