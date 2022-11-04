FROM python:3.9-slim
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
# Arg to get the repository
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY static static
COPY templates templates
COPY main.py main.py
COPY config.py config.py
COPY requirements.txt requirements.txt
COPY requirements-xia.txt requirements-xia.txt
# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install -r requirements-xia.txt
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
