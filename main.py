import requests
from pypdf import PdfReader
from dotenv import load_dotenv
import os
import time
import sys

load_dotenv()    ## Load environment variables from .env file

api_key = os.getenv("FREETTS_API_KEY")
tts_url = "https://freetts.org/api/v1/tts"

## Extracting text from a pdf:

reader = PdfReader("check.pdf")
for page in reader.pages:
    text = page.extract_text()

    ## Sending a post request to API
    if text:
        payload = {
            "text": text,
            "voice": "en-US-JennyNeural",
            "output_format": "mp3"
        }
        headers = {
            "x-api-key": api_key }
        response = requests.post(tts_url, json=payload, headers=headers)

        ## Handling Error Responses

        if response.status_code == 200:

            audio_content = response.content
            with open("output.mp3", "ab") as audio_file:
                audio_file.write(audio_content)

            print(f"Audio for page {reader.pages.index(page) + 1} saved successfully.")
        else:
            print(f"Failed to generate audio for page {reader.pages.index(page) + 1}. Status code: {response.status_code}")
    else:
        print(f"No text found on page {reader.pages.index(page) + 1}.")

    ## Sleep for 1 second to avoid hitting rate limits
    time.sleep(1)  
