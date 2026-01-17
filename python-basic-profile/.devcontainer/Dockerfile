FROM mcr.microsoft.com/devcontainers/python:3.11

# Install core Python tools inside the container
RUN pip install --no-cache-dir \
    black \
    flake8 \
    mypy \
    pytest \
    ipykernel

# Register the kernel for Jupyter
RUN python -m ipykernel install --user --name python-basic --display-name "Python (Basic)"
