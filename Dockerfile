FROM python:3.10

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 5000
RUN chmod 755 ./entrypoint.sh
CMD ["./entrypoint.sh"]
# ENTRYPOINT ["./entrypoint.sh"]
