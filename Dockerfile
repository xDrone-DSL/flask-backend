FROM python:3.7
RUN pip install pipenv

COPY . .

RUN pipenv install

CMD pipenv run python server.py
