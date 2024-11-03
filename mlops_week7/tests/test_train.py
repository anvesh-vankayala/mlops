import pytest
import json
import re
import hydra
from pathlib import Path
import rootutils

# Setup root directory
root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

print('Project root >>>>>>>>>>>>> :', root)

# Import train function
from src.train import train
import logging
from datetime import datetime
import time


@pytest.fixture
def config():
    with hydra.initialize(version_base=None, config_path="../configs"):
        cfg = hydra.compose(
            config_name="train.yaml",
            overrides=["experiment=dogbreed_ex_train",
                       "trainer.max_epochs=3",
                       "test=True"],
        )

        # Override paths in the config
        project_root = rootutils.find_root(indicator=".project-root")
        cfg.paths.root_dir = str(project_root)
        cfg.paths.data_dir = str(project_root / "data")
        cfg.paths.log_dir = str(project_root / "logs")
        cfg.paths.output_dir = str(project_root / "outputs")
        cfg.paths.work_dir = str(project_root)
        return cfg

def parse_metrics_from_console_output(caplog):
    """Parse metrics from the captured console output."""
    for record in caplog.records:
        if "'val/acc':" in record.getMessage():
            print('Entered if condition >>>>>>>>>>>>>>>>>>>>>> -------------------')
            # Extract the dictionary-like string
            metrics_str = re.search(r'{.*}', record.getMessage()).group(0)
            print('metrics string --  -------------------',metrics_str)
            # Parse individual values using regex
            metrics = {}
            pattern = r"'([\w/]+)': tensor\(([\d.]+)\)"
            # pattern = r"'(\w+)': tensor\(([\d.]+)\)"
            matches = re.finditer(pattern, metrics_str)
            
            for match in matches:
                key = match.group(1)
                value = float(match.group(2))
                metrics[key] = value
                
            return metrics
    return None

@pytest.fixture
def caplog(caplog):
    """Fixture to ensure caplog captures the right log level"""
    caplog.set_level(logging.INFO)
    return caplog

@pytest.mark.order(1)
def test_dogbreed_ex_training(config, tmp_path, caplog):
    # Update output and log directories to use temporary path
    config.paths.output_dir = str(tmp_path)
    config.paths.log_dir = str(tmp_path / "logs")
    
    print('>>>>>>>>>>>>>>>----->',config)
    # Run training
    train(config)
    
    # Parse metrics from console output
    metrics = parse_metrics_from_console_output(caplog)
    
    # Debug output
    print("All captured logs:")
    for record in caplog.records:
        print(record.getMessage())
    print(f"Parsed metrics: {metrics}")
    
    # Assert metrics were found and validation accuracy meets threshold
    assert metrics is not None, "Could not find metrics in console output"
    print(f'metrics >>>>  {metrics}')
    val_acc = metrics['val/acc']
    assert val_acc > 0.30, f"Validation accuracy {val_acc} is not greater than 0.30"