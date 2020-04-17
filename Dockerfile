FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN cd /app
RUN pip3 install -r requirements.txt
