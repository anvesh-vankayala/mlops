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
    - 8, For hyper parameter tuning using optuna, run train.py by passing params
        ````
         python src/train.py -m hparams=dogbreed_ex_vit_hparam ++trainer.log_every_n_steps=5
        ````

- ### Detailed TODO's :    
    - Create simple traning pipeline first, with hydra configurations. - Done
    - Integrate CI CD wirh github actions - Done
    - CI CD to be created for training cycle by publishing the score n logs.
    - Adding loggers to the hydra configuration - Done
    - Hyperparmeter tuning with optuna - Done
    - Adding LR finder and Batch size optimization
    - Test cases to be added - Done
    - Test cases to be added as part of CI CD pipeline
    - DVC configuration to be added, for managing data versioning with DVC.
    - Dockerization of the flow.
    - Publishning as a package in github. 
    - Add Mlflow and comet part of training and test tracking. - Done
    - Codecoverage - Done
        - codecov.io :   https://docs.codecov.com/reference/overview
        - token for MlOps repo:00c7d035-21b1-4cf0-b503-464d7db3d6c2
        - Codecov url : https://app.codecov.io/gh/anvesh-vankayala
        - mlops dash board : https://app.codecov.io/gh/anvesh-vankayala/mlops/tree/main/mlops_week7%2Fsrc%2Fmodels 


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



## TPE Optimizer :

Tree-structured Parzen Estimator (TPE) Explained
- Overview
    TPE is a Bayesian optimization algorithm specifically designed for hyperparameter tuning that offers advantages over traditional methods like Grid Search and Random Search. The key difference is that TPE learns from previous trials to make informed decisions about which hyperparameter combinations to try next, rather than using pure trial and error.
    Core Components
- 1. Bayesian Optimization Framework
    TPE uses a Bayesian approach to update beliefs about optimal hyperparameters based on previous results
    It maintains probability distributions over hyperparameter values that are likely to perform well
- 2. Two-Distribution Approach.
    TPE divides the observed hyperparameter configurations into two distributions:
    l(x): The "good" distribution containing hyperparameter configurations that performed in the top γ percentile
    g(x): The "bad" distribution containing all other configurations
    Typically γ is set to 0.2 (top 20%)
- 3. Parzen Estimation (Kernel Density Estimation)
    - Used to model both l(x) and g(x) distributions
      Creates probability distributions by averaging across multiple normal distributions centered on observed data points
    - Higher density in regions where good hyperparameter combinations are clustered
### How TPE Works
- Initial Exploration:
    Starts with random sampling from prior distributions for each hyperparameter
    Builds initial understanding of the hyperparameter space
- Distribution Modeling:
    Splits observed results into l(x) and g(x) based on performance
    Uses Parzen Estimation to model these distributions
- Selection Strategy:
    Selects next hyperparameters by maximizing the ratio g(x)/l(x)
    This favors regions that are more likely under l(x) than g(x)
    Effectively balances exploration and exploitation

### Advantages
- Efficient Search:
    More efficient than Grid/Random Search as it learns from previous trials
    Focuses on promising regions of the hyperparameter space
- Adaptability:
    Can handle both continuous and discrete hyperparameters
    Works well with conditional hyperparameters
- Scalability:
    Suitable for high-dimensional hyperparameter spaces
    Computationally efficient compared to other Bayesian optimization methods

### Implementation Considerations
- Prior Selection:
    Initial hyperparameter ranges should be reasonable
    Poor priors can slow down convergence
- Quantile Threshold (γ):
    Typically set to 0.2
    Too high values reduce samples in l(x)
    Too low values may lead to premature convergence
- Number of Initial Samples:
    Need enough initial samples for reliable distribution estimation
    Typically 20-30 random samples to start
### Source
- Source: Building a Tree-Structured Parzen Estimator from Scratch
          https://towardsdatascience.com/building-a-tree-structured-parzen-estimator-from-scratch-kind-of-20ed31770478
- Source: Tree-Structured Parzen Estimator: Understanding Its Algorithm Components\
          https://arxiv.org/abs/2304.11127  

- TPE has become increasingly popular in modern machine learning frameworks and is implemented in libraries like Hyperopt and Optuna for automated hyperparameter optimization.




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