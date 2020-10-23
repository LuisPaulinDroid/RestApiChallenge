FROM python:3.6.1-alpine

WORKDIR /RestApiChallenge

# Copying all project files to workdir
COPY . /RestApiChallenge

# Upgrading pip and installing dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

#Default file to excecute
CMD ["python","run.py"]