from openai import OpenAI
from dotenv import load_dotenv
import os
def get_openai_client():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)