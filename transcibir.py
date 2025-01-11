import speech_recognition as sr

# Inicializa el reconocedor de voz
recognizer = sr.Recognizer()

# Cargar el archivo de audio
audio_file = "ruta/a/tu/archivo_de_audio.wav"

# Abre el archivo y reconoce el audio
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)

# Intenta reconocer el audio
try:
    text = recognizer.recognize_google(audio, language='es-ES')
    print(f"Texto reconocido: {text}")
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print(f"No se pudo conectar al servicio de Google Speech Recognition; {e}")
