## Project workflow:

- ### Setup
    - Install UV
    ````
    pip install uv
    ````

    - Initialize UV with in the directory, which creates pyproject.toml, sample.py, with .python-version
    ````
    uv init
    ````

    - Install hydra with pip
    ````
    pip install hydra-core --upgrade
    ````

    - Create configs directory with model configs, dataset configs and train.yaml
    - Create .githubs/workflows with ci.yaml (for CI/CD pipeline)

- ### TODO
    - Create simple traning pipeline first, with hydra configurations.
    - CI CD to be created for training cycle by publishing the score n logs.
    - Adding loggers to the hydra configuration
    - Hyperparmeter tuning with optuna
    - Adding LR finder and Batch size optimization
    - Test cases to be added
    - Test cases to be added as part of CI CD pipeline
    - DVC configuration to be added, by saving trained and finalized model in DVC.
    - Dockerization of the flow.
    - Publishning as a package in github. 