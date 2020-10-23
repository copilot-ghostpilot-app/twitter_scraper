FROM python:3

COPY ./requirements.txt /

RUN pip install -r /requirements.txt

COPY ./scraper /scraper

WORKDIR /scraper

CMD ["/scraper/main.py"]