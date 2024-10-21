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
