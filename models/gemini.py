# import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv() #to load the environment variables from the .env file

# class GeminiModel:
#     def __init__(self, gemini_api, model_name):
#         # Configure the API with the provided key
#         genai.configure(api_key = os.getenv("Genai_api"))
        
#         # Default configuration settings; can be customized further if needed
#         generation_config = {
#             "temperature": 0,
#             "top_p": 1,
#             "top_k": 1,
#             "max_output_tokens": 30720,
#         }
        
#         safety_settings = [
#             {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
#             {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
#             {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
#             {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
#         ]
        
#         # Set up the model with the provided model name
#         self.model = genai.GenerativeModel(model_name="gemini-1.5-flash",
#                                            generation_config=generation_config,
#                                            safety_settings=safety_settings)

#     def generate_content(self, prompt):
#         # Generate content based on the provided prompts
#         response = self.model.generate_content([prompt])
#         return response.text
import google.generativeai as genai
from typing import Optional

class GeminiModel:
    def __init__(self, gemini_api: str, model_name: str):
        # Configure Google API
        gemini_api = os.getenv("Genai_api")
        genai.configure(api_key=gemini_api)
        
        # Generation config
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 30720,
        }
        
        # Safety settings
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
        ]
        
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            safety_settings=safety_settings
        )

    def generate_content(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text