import requests
from pypdf import PdfReader
from dotenv import load_dotenv
import os
import time
import sys

load_dotenv()    # Load environment variables from .env file

api_key = os.getenv("FREETTS_API_KEY")
tts_url = "https://freetts.org/api/v1/tts"


