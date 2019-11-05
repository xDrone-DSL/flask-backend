# Setup

To run it in Docker:

1. `docker build -t xdronedsl/backend .` 

2. `docker run -it xdronedsl/backend`  

To run it without Docker:  
1. Make sure you're using python 3
If `pip --version` mentions python 2, then use `pip3` instead of `pip` and `python3` instead of `python` in the commands below.

    {Tip: 
    Add `alias python=python3` and `alias pip=pip3`in `~/.bashrc`, and run `source ~/.bashrc` 

    OSX: `source ~/.bashrc` will (probably) not be run after rebooting, so add `source ~/.bashrc` to `~/.profile`
          (Source: http://archive.is/Q0EUC) }


2. Install pipenv
`pip install --user pipenv`

3. Enter the pipenv environment
In this directory run:
`pipenv shell`

(If this doesnt work, try: `sudo apt install pipenv`or `brew install pipenv`first, and then try again)

4. Install the env dependencies `pipenv install --dev`

5. To run the server run `python server.py`
