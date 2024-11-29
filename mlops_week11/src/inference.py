import gradio as gr
import torch
import torchvision.transforms as transforms
from PIL import Image
from gradio.flagging import SimpleCSVLogger
import onnxruntime as ort
import os
from pathlib import Path
import numpy as np


class DogBreedClassifier:
    def __init__(self):
        # Get absolute path to the model file
        project_root = Path(__file__).resolve().parents[1]  # Go up 2 levels to reach project root
        model_path = project_root / "model_storage" / "model.onnx"
        
        if not model_path.exists():
            raise FileNotFoundError(
                f"ONNX model not found at {model_path}. "
                "Please run the onnx_converter.py first."
            )
            
        self.device = torch.device('cpu')
        self.model = ort.InferenceSession(str(model_path))  # Convert Path to string

        # Define the same transforms used during training/testing
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        # Class labels based on dogbreed.yaml
        self.labels = ['Beagle', 'Boxer', 'Bulldog', 'Dachshund', 'German_Shepherd', 'Golden_Retriever', 'Labrador_Retriever', 'Poodle', 'Rottweiler', 'Yorkshire_Terrier']

    @torch.no_grad()
    def predict(self, image):
        if image is None:
            return None
        
        # Convert to PIL Image if needed
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image).convert('RGB')
        
        # Preprocess image
        img_tensor = self.transform(image).unsqueeze(0).numpy()  # Convert to numpy array for ONNX model
        
        # Get prediction
        output = self.model.run(None, {self.model.get_inputs()[0].name: img_tensor})
        probabilities = torch.nn.functional.softmax(torch.tensor(output[0]), dim=1)
        
        # Create prediction dictionary
        return {
            self.labels[idx]: float(prob)
            for idx, prob in enumerate(probabilities[0])
        }

# Create classifier instance
classifier = DogBreedClassifier()

# Create Gradio interface
demo = gr.Interface(
    fn=classifier.predict,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=len(classifier.labels)),
    title="Dog Breed Classifier",
    description="Upload an image to classify the breed of the dog",
    flagging_mode="never",
    flagging_callback=SimpleCSVLogger()
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080,share=True) 
