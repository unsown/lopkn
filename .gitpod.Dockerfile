FROM gitpod/workspace-full-vnc:latest

USER root

# Install Dropbear SSH server
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qy && apt-get install -qy \
        netcat \
        openssh-server \
        dropbear \
        tmux \
        vim

RUN apt-get install -qy \
      pulseaudio `# get a dummy sink`

# Install Chisel
RUN curl https://i.jpillora.com/chisel! | bash
