# Início →

# pip install SpeechRecognition

# Grava o áudio a ser convertido (Recomendado o Audacity)
# Exporte-o no formato WAV

# No código utilizamos a biblioteca SpeechRecognition para:
# - Ler o arquivo audio.wav (que exportamos no Audacity)
# - Enviar para a API do Google Speech-to-Text
# - Mostrar o resultado

import speech_recognition as sr

# Instancia a classe Recognizer
r = sr.Recognizer()

# Lê o arquivo do áudio
with sr.AudioFile("./audio.wav") as fonte:
    audio = r.record(fonte)

# Utiliza o Google Speech Recognition para fazer a conversão
try:
    # Utiliza a chave de API padrão do próprio Speech SpeechRecognition
    # Para utilizar uma chave própria (recomendada), acesse a documentação
    texto = r.recognize_google(audio, language='pt-br')
    print(f'Google Speech Recognition acha que você disse: \n "{texto}"')
except sr.UnknowValueError:
    print('Google Speech Recognition não entendeu seu áudio.')
except sr.RequestError as erro:
    print(f'Não foi possível se conectar à API da Google. Erro: {str(erro)}')

# ← Fim