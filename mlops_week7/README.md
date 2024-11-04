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