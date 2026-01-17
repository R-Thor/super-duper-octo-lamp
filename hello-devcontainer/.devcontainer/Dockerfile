FROM ubuntu:22.04

# Create the vscode user (VS Code expects this)
RUN apt-get update && apt-get install -y sudo \
    && useradd -m vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
