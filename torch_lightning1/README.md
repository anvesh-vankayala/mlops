## Lighting module


## Sample Docker file::

# FROM ubuntu:latest
FROM python:3.9-slim

WORKDIR /workspace
COPY train.py /workspace/
# COPY requirements.txt /workspace/

RUN pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install --no-cache-dir lightning

CMD ["python", "train.py"]