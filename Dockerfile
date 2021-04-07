# Pulls from public python 3 image file.
FROM python:3

# Sets the working directory in the Container
WORKDIR /usr/src/app

# Copies all files in the current directory into working directory in Container.
COPY . . 

# Installs all dependencies of the Flask app.
RUN pip install -r requirements.txt

# Executes the web application file. 
CMD [ "python3", "./web_app.py" ]