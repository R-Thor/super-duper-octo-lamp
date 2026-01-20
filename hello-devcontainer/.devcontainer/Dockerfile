FROM ubuntu:22.04

# Create the vscode user
RUN apt-get update && apt-get install -y sudo \
    && useradd -m vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install basic tools devcontainers expect
RUN apt-get install -y curl git bash

# Add your custom entrypoint
COPY entrypoint.sh /usr/local/bin/devcontainer-entrypoint
RUN chmod +x /usr/local/bin/devcontainer-entrypoint

ENTRYPOINT ["/usr/local/bin/devcontainer-entrypoint"]
