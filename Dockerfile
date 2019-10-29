FROM kennethreitz/pipenv

COPY . .

RUN pipenv install

CMD pipenv run python server.py
