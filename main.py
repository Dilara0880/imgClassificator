import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import torch
from torchvision import models, transforms
import urllib.request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

model = models.resnet50(pretrained=True)
model.eval()

labels_url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
class_names = urllib.request.urlopen(labels_url).read().decode("utf-8").splitlines()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def classify_image(image_path):
    image = Image.open(image_path)
    image_tensor = preprocess(image)
    image_tensor = image_tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(image_tensor)
    _, predicted_idx = torch.max(output, 1)
    predicted_class = class_names[predicted_idx.item()]
    return predicted_class[1:-2]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def classify(request: Request):
    formdata = await request.form()
    image_file = formdata["file"]
    cur_dir = os.getcwd()
    if image_file.filename != '':
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
    image_path = f"{cur_dir}/uploads/{image_file.filename}"
    with open(image_path, "wb") as image:
        image.write(await image_file.read())
    class_name = classify_image(image_path)
    image = Image.open(image_path)
    width, height = image.size
    return templates.TemplateResponse("result.html", {
        "request": request,
        "width": width,
        "height": height,
        "class_name": class_name,
    })


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
