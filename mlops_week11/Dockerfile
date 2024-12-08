FROM --platform=linux/amd64 public.ecr.aws/docker/library/python:3.12-slim
# FROM public.ecr.aws/docker/library/python:3.11.10-slim



# Copy the Lambda adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

# Set environment variables
ENV PORT=8000

# Set working directory
WORKDIR /var/task

# RUN pip install setuptools 

# Copy requirements first to leverage Docker cache
COPY requirements-infer.txt ./
# RUN pip install --no-cache-dir -r requirements-infer.txt
RUN pip install --no-cache-dir setuptools && \
    pip install --no-cache-dir -r requirements-infer.txt

# Copy application code and model
# Start of Selection
# COPY . ./
# COPY app.py ./
# COPY icons.py ./
# COPY model_storage/model.onnx ./

COPY app.py icons.py model_storage/model.onnx ./


# COPY app.py ./
# COPY icons.py ./
# COPY model.onnx ./

# Set command
CMD exec uvicorn --host 0.0.0.0 --port $PORT app:app 