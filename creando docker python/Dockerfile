FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app/project

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

