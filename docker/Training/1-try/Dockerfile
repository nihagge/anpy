FROM debian:jessie
RUN apt-get update
RUN apt-get install -y \
    git \
#    vim \
#    lynx \
#    screen \
#    tmux \
    htop
WORKDIR /opt
COPY abc.txt /etc/abc.txt
COPY abc.txt def.txt
#CMD ["echo", "Hallo World"]
