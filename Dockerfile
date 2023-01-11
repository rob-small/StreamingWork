FROM python:3

COPY app.py mydevice.py .

RUN pip install Flask
RUN pip install numpy

CMD [ "python", "./app.py" ]