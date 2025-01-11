import speech_recognition as sr

# Inicializa el reconocedor de voz
recognizer = sr.Recognizer()

# Usa el micrófono para capturar el audio
with sr.Microphone() as source:
    print("Por favor, hable ahora.")
    audio = recognizer.listen(source)

# Intenta reconocer el audio
try:
    text = recognizer.recognize_google(audio, language='es-ES')  # Usando Google Web Speech API
    print(f"Texto reconocido: {text}")
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print(f"No se pudo conectar al servicio de Google Speech Recognition; {e}")
