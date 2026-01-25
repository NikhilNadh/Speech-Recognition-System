import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            print("🎧 Loading audio file...")
            audio_data = recognizer.record(source)

        print("📝 Transcribing...")
        text = recognizer.recognize_google(audio_data)

        return text

    except sr.UnknownValueError:
        return "❌ Sorry, I could not understand the audio."
    except sr.RequestError:
        return "❌ API Error: Please check your internet connection."
    except FileNotFoundError:
        return "❌ File not found. Please check the audio file path."

if __name__ == "__main__":
    print("📌 SPEECH RECOGNITION SYSTEM (Speech-to-Text)\n")

    audio_file = input("Enter audio file path (WAV format recommended): ")

    result = transcribe_audio(audio_file)

    print("\n✅ Transcribed Text:\n")
    print(result)