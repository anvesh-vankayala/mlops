## Lighting module

### EMLOV4-Session-04 Assignment - PyTorch Lightning - I

### PyTorch Lightning - I

#### Requirements:

- Add Dockerfile for the project
    - Create a DevContainer for the Project
    - Docker Image should have your package installed
- Use this dataset: https://www.kaggle.com/datasets/khushikhushikhushi/dog-breed-image-datasetLinks to an external site.
    - You’ll need to Create a DataModule for this
    - You can download using Kaggle API: https://www.kaggle.com/docs/api#interacting-with-datasetsLinks to an external site.
- Add eval.pyLinks to an external site. to load model from checkpoint and run on validation dataset
    - Must print the validation metrics
- Push the repository to GitHub
- Use infer.pyLinks to an external site. to run on 10 images
- Add instructions on README.mdLinks to an external site.
    - How to use docker run to train and eval the model
    - How to Train, Eval, Infer using Docker
    - Make sure to use Volume Mounts!

### Development method
1. Made required folders for model, data loader and data storage
2. Used auto fetch and unload module with gdown module
3. Wrote training script where model has a call back of checkpoint saving module
4. Wrote evaluation script that outputs validation metrics and wrote infer script that infers on 10 images and stores output in infer_images folder
5. Used model_storage as volume mount for all docker containers


### Build Command

```
docker build -t dog_train -f ./Dockerfile .
```

### Docker file usage to train, eval and infer
- Train

```
docker run --rm -v ./model_storage:/workspace/model_storage dog_train python src/train.py --data data --logs logs --ckpt_path model_storage 
```

- Eval

```
docker run --rm -v ./model_storage:/workspace/model_storage dog_train python src/eval.py --data data --ckpt_path "model_storage/epoch=0-checkpoint.ckpt"
```

- Infer

```
docker run --rm -v ./model_storage:/workspace/model_storage -v ./infer_images:/workspace/infer_images dog_train python src/infer.py  --input_folder data/dataset/val/ --output_folder infer_images --ckpt_path "model_storage/epoch=0-checkpoint.ckpt"
```

## Sample Docker file::

# FROM ubuntu:latest
FROM python:3.9-slim

WORKDIR /workspace
COPY train.py /workspace/
# COPY requirements.txt /workspace/

RUN pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install --no-cache-dir lightning

CMD ["python", "train.py"]