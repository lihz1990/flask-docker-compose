From python:3.8-alpine

RUN pip3 install flask requests -i https://pypi.doubanio.com/simple  && mkdir /app

COPY src/app.py /app/

WORKDIR /app
Env FLASK_APP app.py
EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]

