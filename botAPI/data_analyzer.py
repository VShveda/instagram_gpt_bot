import os

import requests
from PIL import Image
from io import BytesIO
import google.generativeai as gemini
from dotenv import load_dotenv


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini.configure(api_key=gemini_api_key)


def download_image(url: str) -> Image:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def img_description(url: str) -> str:
    prompt = "Describe this image: "
    img = download_image(url)
    model = gemini.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, img])
    return response.text
