FROM gitpod/workspace-full

USER root

# Install Dropbear SSH server
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq \
        netcat \
        openssh-server \
        dropbear \
        tmux \
        vim

# Install Chisel
RUN curl https://i.jpillora.com/chisel! | bash
