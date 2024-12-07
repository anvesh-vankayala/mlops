
from typing import Annotated
import io
import numpy as np
import onnxruntime as ort
from PIL import Image
from fastapi import FastAPI, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse, HTMLResponse
from fasthtml import FastHTML
from fasthtml.common import (
    Html,
    Script,
    Head,
    Title,
    Body,
    Div,
    Form,
    Input,
    Img,
    P,
    to_xml,
)
from shad4fast import (
    ShadHead,
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
    CardFooter,
    Alert,
    AlertTitle,
    AlertDescription,
    Button,
    Badge,
    Separator,
    Lucide,
    Progress,
)
import base64
import torch
import torchvision.transforms as transforms
from pathlib import Path

# Create main FastAPI app
app = FastAPI(
    title="Image Classification API",
    description="FastAPI application serving an ONNX model for image classification",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Load the ONNX model
classifier = DogBreedClassifier()

# FastAPI routes
@app.get("/", response_class=HTMLResponse)
async def ui_home():
    content = Html(
        Head(
            Title("Dog Breed Classifier"),
            ShadHead(tw_cdn=True, theme_handle=True),
            Script(
                src="https://unpkg.com/htmx.org@2.0.3",
                integrity="sha384-0895/pl2MU10Hqc6jd4RvrthNlDiE9U1tWmX7WRESftEDRosgxNsQG/Ze9YMRzHq",
                crossorigin="anonymous",
            ),
        ),
        Body(
            Div(
                Card(
                    CardHeader(
                        Div(
                            CardTitle("Dog Breed Classifier 🐶"),
                            Badge("AI Powered", variant="secondary", cls="w-fit"),
                            cls="flex items-center justify-between",
                        ),
                        CardDescription(
                            "Upload an image to classify the breed of the dog. Our AI model will analyze it instantly!"
                        ),
                    ),
                    CardContent(
                        Form(
                            Div(
                                Div(
                                    Input(
                                        type="file",
                                        name="file",
                                        accept="image/*",
                                        required=True,
                                        cls="mb-4 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary file:text-primary-foreground hover:file:bg-primary/90 file:cursor-pointer",
                                    ),
                                    P(
                                        "Drag and drop an image or click to browse",
                                        cls="text-sm text-muted-foreground text-center mt-2",
                                    ),
                                    cls="border-2 border-dashed rounded-lg p-4 hover:border-primary/50 transition-colors",
                                ),
                                Button(
                                    Lucide("sparkles", cls="mr-2 h-4 w-4"),
                                    "Classify Image",
                                    type="submit",
                                    cls="w-full",
                                ),
                                cls="space-y-4",
                            ),
                            enctype="multipart/form-data",
                            hx_post="/predict",
                            hx_target="#result",
                        ),
                        Div(id="result", cls="mt-6"),
                    ),
                    cls="w-full max-w-3xl shadow-lg",
                    standard=True,
                ),
                cls="container flex items-center justify-center min-h-screen p-4",
            ),
            cls="bg-background text-foreground",
        ),
    )
    return to_xml(content)


@app.post("/predict", response_class=HTMLResponse)
async def predict(file: Annotated[bytes, File(description="Image file to classify")]):
    try:
        image = Image.open(io.BytesIO(file))
        response = classifier.predict(image)
        image_b64 = base64.b64encode(file).decode("utf-8")

        predicted_class = max(response.items(), key=lambda x: x[1])[0]
        confidence = max(response.values())

        # Emoji mapping
        emoji_map = {label: "🐶" for label in classifier.labels}

        # Create the results display with grid layout
        results = Div(
            Div(
                # Left column - Image
                Div(
                    Img(
                        src=f"data:image/jpeg;base64,{image_b64}",
                        alt="Uploaded image",
                        cls="w-full rounded-lg shadow-lg aspect-square object-cover",
                    ),
                    cls="relative group",
                ),
                # Right column - Results
                Div(
                    Badge(
                        f"It's a {predicted_class.lower()}! {emoji_map[predicted_class]}",
                        variant="outline",
                        cls=f"{'bg-green-500/20 hover:bg-green-500/20 border-green-500/50' if confidence > 0.8 else 'bg-yellow-500/20 hover:bg-yellow-500/20 border-yellow-500/50'} text-lg",
                    ),
                    # Confidence Progress Section
                    Div(
                        Div(
                            P("Confidence Score", cls="font-medium"),
                            P(
                                f"{confidence:.1%}",
                                cls=f"text-xl font-bold",
                            ),
                            cls="flex justify-between items-baseline",
                        ),
                        Progress(
                            value=int(confidence * 100),
                            cls="h-2",
                        ),
                        cls="mt-4 space-y-2",
                    ),
                    Separator(cls="my-4"),
                    # Detailed Analysis Section
                    P("Detailed Analysis", cls="font-medium mb-2"),
                    Div(
                        *[
                            Div(
                                Div(
                                    P(f"{label} {emoji_map[label]}", cls="font-medium"),
                                    P(
                                        f"{prob:.1%}",
                                        cls=f"font-medium { "" if label == predicted_class else 'text-muted-foreground'}",
                                    ),
                                    cls="flex justify-between items-center",
                                ),
                                Progress(
                                    value=int(prob * 100),
                                    cls="h-2",
                                ),
                                cls="space-y-2",
                            )
                            for label, prob in response.items()
                        ],
                        cls="space-y-4",
                    ),
                ),
                cls="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            cls="animate-in fade-in-50 duration-500",
        )

        return to_xml(results)

    except Exception as e:
        error_alert = Alert(
            AlertTitle("Error ❌"),
            AlertDescription(str(e)),
            variant="destructive",
            cls="mt-4",
        )
        return to_xml(error_alert)


@app.get("/health")
async def health_check():
    return JSONResponse(
        content={"status": "healthy", "model_loaded": True}, status_code=200
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)