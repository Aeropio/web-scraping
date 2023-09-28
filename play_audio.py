import pyttsx3
from PyPDF2 import PdfReader


def play_audio(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text = page.extract_text()

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def text_to_audio(input_file):
    reader = PdfReader(input_file)
    audio_content = ""
    for page in reader.pages:
        text = page.extract_text()
        audio_content += text + " "

    engine = pyttsx3.init()
    engine.save_to_file(audio_content, f"uploads/{input_file.split('.')[0]}.mp3")
    engine.runAndWait()
    engine.stop()  # Stop the engine after running
