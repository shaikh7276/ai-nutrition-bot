import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyAb5s0dTp12BOOqtYaHEscLMJ1_b0KLKQE"))

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)
