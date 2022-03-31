FROM ubuntu:20.04

RUN apt-get install -y apt-transport-https && \
     apt-get -qq update && \
     apt-get -y install \
     software-properties-common \
     sudo && \
     apt-get -yqq install --install-recommends \
     firefox \
     libxrender1 \
     libxcomposite1 \
     libgtk-3-dev \
     xvfb \
     libjpeg8-dev \
     libjpeg-dev \
     libwebp-dev \
     zlib1g-dev \
     ffmpeg \
     libdbus-glib-1-2 \
     python-dev \
     python3-pip \
     libssl-dev \
     g++ && \
     apt-get -yqq clean && \
     rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/pin -m -s /bin/bash pin && \
     echo pin:pin | chpasswd && \
     echo 'pin ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/pin && \
     chmod 0440 /etc/sudoers.d/pin

USER pin

ENV PATH="${PATH}:/home/pin/.local/bin"

RUN mkdir /home/pin/.local/ && \
     mkdir /home/pin/.local/bin && \
     mkdir /home/pin/app

WORKDIR /home/pin/app

COPY pyproject.toml poetry.lock ./
COPY deps/geckodriver /home/pin/.local/bin/geckodriver

RUN pip install -U pip && \
     pip install poetry==1.1.13 && \
     poetry config virtualenvs.create false && \
     poetry install --no-root
