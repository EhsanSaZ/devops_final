FROM ubuntu:latest

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . ./

#CMD ["python3", "./tictactoe.py"]