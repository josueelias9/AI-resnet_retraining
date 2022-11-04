FROM python:3.9.15

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "keep_server_alive.py" ]

