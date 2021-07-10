# Início →

# pip install pytube

from pytube import YouTube

# Cria objeto com URL do vídeo a ser baixado.
video = YouTube(input('Cole aqui a URL do vídeo a ser baixado: '))

# Configura a melhor qualidade de vídeo.
stream = video.streams.get_highest_resolution()

# Faz o download do vídeo e o salva na pasta "saida".
stream.download(output_path='./saida')

# ← Fim