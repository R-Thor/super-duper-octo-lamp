#!/bin/bash
set -e

# If VS Code passes UID/GID, use them; otherwise default to the container's values
USER_UID=${USER_UID:-1000}
USER_GID=${USER_GID:-1000}

# Update the vscode user's UID/GID if needed
if [ "$(id -u vscode)" != "$USER_UID" ]; then
    usermod -u "$USER_UID" vscode
fi

if [ "$(id -g vscode)" != "$USER_GID" ]; then
    groupmod -g "$USER_GID" vscode
fi

# Fix permissions on the home directory
chown -R vscode:vscode /home/vscode || true

# Execute whatever command VS Code wants to run
exec "$@"
