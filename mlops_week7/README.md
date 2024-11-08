## Project workflow:

- ### Setup
    - 1, Install UV
        ````
        pip install uv
        ````

    - 2, Initialize UV with in the directory, which creates pyproject.toml, sample.py, with .python-version
        ````
        uv init
        ````

    - 3, Install hydra with pip
        ````
        pip install hydra-core --upgrade
        ````

    - 4, Create configs directory with model configs, dataset configs and train.yaml
    - 5, Create .githubs/workflows with ci.yaml (for CI/CD pipeline)
    - 6, Create virtual env with specific python version and activate with uv
        ````
        uv venv my_env --python 3.11
        source my_env/bin/activate
        ````
    - 7, Install dependencies from pyprojects.toml file,
        ````
        uv pip install -r pyproject.toml
        ````

- ### Detailed TODO's :    
    - Create simple traning pipeline first, with hydra configurations. - Done
    - CI CD to be created for training cycle by publishing the score n logs.
    - Adding loggers to the hydra configuration - Done
    - Hyperparmeter tuning with optuna 
    - Adding LR finder and Batch size optimization
    - Test cases to be added
    - Test cases to be added as part of CI CD pipeline
    - DVC configuration to be added, by saving trained and finalized model in DVC.
    - Dockerization of the flow.
    - Publishning as a package in github. 
    - Add Mlflow and comet part of training and test tracking. - Done
    - Codecoverage : https://docs.codecov.com/reference/overview
      token:13a0aa3e-424f-4802-8518-562560b7fe23
            00c7d035-21b1-4cf0-b503-464d7db3d6c2


##  Features to be attempted :
- To Run Hyper Param Optimization with Github Actions
- Your CI/CD Action will add a comment at the end with a list of all hparams, and it's test accuracy in a table format
- Plot combined metrics for all runs (val/loss & val/acc)
- Optimize Params for any of these models:
    - https://github.com/huggingface/pytorch-image-models/blob/main/timm/models/mambaout.pyLinks to an external site.
    - https://github.com/huggingface/pytorch-image-models/blob/main/timm/models/convnext.pyLinks to an external site.
    - https://github.com/huggingface/pytorch-image-models/blob/main/timm/models/volo.pyLinks to an external site.
- Dataset
- Any! Just don't choose a really large dataset
- You can use DVC, like the last assignment
- Perform at least 10 experiments, choose a smaller model so it doesn't take time.
- Each experiment should run for at least 2 epochs
- Before running the experiments, see if your model works with your hyper parameters options
- Use Cursor for suggesting the hyper parms and creating the hparams.yaml file



## pyproject.toml

[project]
name = "mlops-week7"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11.7"
dependencies = [
    "lightning[extra]==2.1.0",
    "loguru>=0.7.2",
    "rich>=13.9.2",
    "timm>=1.0.9",
    "torch @ https://download.pytorch.org/whl/cpu/torch-2.4.0%2Bcpu-cp311-cp311-linux_x86_64.whl",
    "torchvision @ https://download.pytorch.org/whl/cpu/torchvision-0.19.0%2Bcpu-cp311-cp311-linux_x86_64.whl",
    "torchmetrics>=1.0.3",
    "rootutils==1.0.7",
    "hydra-core==1.3.0",
    "comet-ml>=3.31.0",
    "mlflow>=1.0.0",
    "pytest==8.3.3",
    "pytest-cov==5.0.0",
    "coverage==7.6.3",
    "pytest-order==1.3.0",
    "pytest-ordering==0.6",
    "pytest-dependency==0.6.0",

]

[tool.pip]
extra-index-url = "https://download.pytorch.org/whl/cpu"