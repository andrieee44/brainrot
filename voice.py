from text import generate_transcript
import google.cloud.texttospeech as tts
import requests

idkwhatthisis = "sk_3a4900de4018ef374e87ad2d41f32847b83c72f7333300cf"

def generate_audio_neets(narration, fp):
    response = requests.request(
        method="POST",
        url="https://api.neets.ai/v1/tts",
        headers={
            "Content-Type": "application/json",
            "X-API-Key": "c0d9aeeef6f14e98ad46c8d23e24535b"
        },
        json={
            "text": narration,
            "voice_id": "us-male-15",
            "params": {
                "model": "ar-diff-50k"
            }
        }
    )

    with open(fp, "wb") as f:
        f.write(response.content)

def generate_audio_google(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"./{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
        

if __name__ == "__main__":
    test_file = "C:/Users/abyam/Desktop/Research-Project/examples/Topic 3 Cellular Respiration.pdf"
    transcript = generate_transcript(test_file)
    print(transcript["narration"])
    generate_audio_google("en-US-Journey-D", transcript["narration"])