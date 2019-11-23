FROM arm32v7/telegraf:latest

RUN apt-get update && apt-get install -y python3
RUN rm -fr /var/lib/apt/lists/*

COPY telegraf.conf /etc/telegraf/telegraf.conf
COPY sensors.py /sensors.py