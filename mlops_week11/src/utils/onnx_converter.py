import sys
import torch
import onnx
from pathlib import Path

def add_project_root_to_path():
    """Add the project root to the Python path."""
    project_root = str(Path(__file__).resolve().parents[2])  # Go up 2 levels from utils to reach.
    sys.path.append(project_root)

def load_model(checkpoint_path):
    """Load the model from the specified checkpoint file."""
    from src.models.dogbreed_classifer import TimmClassifier
    model = TimmClassifier(base_model="mobilenetv3_small_100", num_classes=10)
    model.load_state_dict(torch.load(checkpoint_path, weights_only=True)['state_dict'])
    model.eval()
    return model

def export_model_to_onnx(model, onnx_path, sample_input):
    """Export the model to ONNX format."""
    torch.onnx.export(model, sample_input, onnx_path, export_params=True, opset_version=11, do_constant_folding=True)

def check_onnx_model(onnx_path):
    """Check the validity of the ONNX model."""
    try:
        onnx_model = onnx.load(onnx_path)
        onnx.checker.check_model(onnx_model)
        print(f'Model has been converted to ONNX format and saved at {onnx_path}')
    except Exception as e:
        print(f'Model is not valid: {str(e)}')

def main():
    add_project_root_to_path()
    
    # Search for .ckpt files in the model_storage folder
    model_storage_path = Path(__file__).resolve().parents[2] / 'model_storage'
    checkpoint_files = list(model_storage_path.glob('*.ckpt'))

    if checkpoint_files:
        # Load the model from the first .ckpt file found
        checkpoint_path = str(checkpoint_files[0])
        model = load_model(checkpoint_path)

        # Define a sample input tensor
        sample_input = torch.randn(1, 3, 224, 224)  # Example for an image input

        # Export the model to ONNX format in the same folder
        onnx_path = str(model_storage_path / 'model.onnx')
        export_model_to_onnx(model, onnx_path, sample_input)
    else:
        print("No .ckpt file found in the model_storage folder.")

    # Check the ONNX model
    check_onnx_model(onnx_path)

if __name__ == "__main__":
    main()
