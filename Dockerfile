FROM "ubuntu:20.04"

ENV DEBIAN_FRONTEND = noninteractive

RUN apt-get update && yes | apt-get upgrade

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir -p /yolo

WORKDIR /yolo/

COPY . .

RUN apt-get install -y git python3-pip

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install jupyter

RUN jupyter notebook --generate-config --allow-root

RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

