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
    - Test cases to be added
    - Test cases to be added as part of CI CD pipeline
    - DVC configuration to be added, by saving trained and finalized model in DVC.
    - 