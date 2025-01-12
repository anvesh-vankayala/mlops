import os
import torch
import argparse
import lightning as L
from lightning.pytorch import Trainer
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning import seed_everything
from models.timm_classifier import TimmClassifier  # Assuming your model is in a file named model.py
from datamodules.dogbreed_datamodule import DogBreedImageDataModule  # Assuming you have a DataModule
import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../configs", config_name="eval",version_base="1.2")
def evaluate_model(cfg: DictConfig):
    print(f"###### --- cfg :- {cfg}")
    # Set seed for reproducibility
    seed_everything(42)

    # Load the model from checkpoint
    model = TimmClassifier.load_from_checkpoint(cfg.model.ckpt_path)
    model.eval()  # Set the model to evaluation mode

    # Initialize the data module
    data_module = DogBreedImageDataModule(dl_path=cfg.model.data_dir)

    # Initialize a trainer
    trainer = Trainer(accelerator='auto', devices=1)

    # Run the test set
    test_results = trainer.test(model, datamodule=data_module)

    print("Test Results:", test_results)

    return test_results

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Infer using trained Dogbreed Classifier")
    # parser.add_argument("--data", type=str, required=True, help="Path to data containing images")
    # parser.add_argument("--ckpt_path", type=str, required=True, help="Path to model checkpoint")
    # args,unknown = parser.parse_known_args()
    # ckpt_path = "./model_storage/model.ckpt"  # Replace with your checkpoint path
    # data_dir = "./data"  # Replace with your data directory
    
    #evaluate_model(args.ckpt_path, args.data)
    ## python src/eval.py model.ckpt_path="./model_storage/epoch0-checkpoint.ckpt" model.data_dir="./my_data"

    evaluate_model()