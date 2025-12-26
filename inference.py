import torch
from torchvision import models, transforms
from PIL import Image
from features import classes, formation, treatments, survival_est
import os
import gdown  # For downloading from Google Drive

# Path where model will be saved
model_path = 'models/classifier.pth'

# Create 'models' folder if it doesn't exist
os.makedirs('models', exist_ok=True)

# Download your trained model from Google Drive if not already present
if not os.path.exists(model_path):
    print("Downloading your trained model from Google Drive...")
    gdown.download(
        "https://drive.google.com/uc?export=download&id=1wrkvA2Tmo9AhJPA_OvL7v8OjN9JgwBFh",
        model_path,
        quiet=False
    )

# Load the model
model = models.resnet50()
model.fc = torch.nn.Linear(model.fc.in_features, 4)  # 4 classes
model.load_state_dict(torch.load(model_path, map_location='cpu'))
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Prediction function
def predict(image_path):
    img = Image.open(image_path).convert('RGB')
    tensor = transform(img).unsqueeze(0)
    
    with torch.no_grad():
        output = model(tensor)
        idx = output.argmax(1).item()
    
    cls = classes[idx]
    return cls, formation[cls], treatments[cls], survival_est[cls]