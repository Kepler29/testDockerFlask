FROM alpine:3.18

RUN apk add py3-pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

CMD [ "python3", "src/app.py" ]