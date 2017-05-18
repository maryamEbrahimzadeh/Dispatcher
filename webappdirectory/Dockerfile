FROM python

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install flask requests

EXPOSE 5000

CMD python3 calc.py
