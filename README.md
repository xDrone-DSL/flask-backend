# Setup

To run it in Docker:

1. `docker build -t xdronedsl/backend .` 

2. `docker run -it xdronedsl/backend`  

To run it without Docker:  
1. Make sure you're using python 3
If `pip --version` mentions python 2, then use `pip3` instead of `pip` and `python3` instead of `python` in the commands below.

2. Install pipenv
`pip install --user pipenv`

3. Enter the pipenv environment
In this directory run:
`pipenv shell`

4. To run the server run `python server.py`
