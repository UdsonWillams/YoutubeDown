import pytube
from pytube.cli import on_progress
from time import sleep

print(56 * "-", "\n")
sleep(1)
print(15 * "-", "BEM VINDO AO YOUTUBEDOWN", 15 * "-", "\n")
sleep(2)
print(25 * "-", "Desenvolvido por: UdsonWillams\n")
sleep(2)
print("Você precisa do link do video para download\nDepois deve escolher o Formato e resolução a serem baixados\n"
      ">>>> ATENÇÃO: OS FORMATOS MARCADOS COMO PROGRESSIVE FALSE PODEM SER BAIXADOS SEM AUDIO <<<<")
sleep(2)
continuar = input("Aperte enter para continuar")
link = input('Digite o link para Download:')
print(" ")
youtube = pytube.YouTube(link, on_progress_callback=on_progress)
videos = youtube.streams.filter(progressive=True)  # .filter(file_extension='mp4') > Com esse comando
# filtraria os videos apenas em mp4
print(f'Seu video > {youtube.title} <\n')
sleep(2)
i = 1
for stream in videos:
    print(str(i) + " " + str(stream) + "\n")
    i += 1
numero_stream = int(input("Diga o numero: "))
video = videos[numero_stream - 1]
print('Baixando...')
video.download()  # 'c:/Users/Public/Videos'
print('DOWNLOAD COMPLETO')
print("Vôce pode achar seu arquivo na mesma pasta que nosso programa está")
fechar = input(" ---- APERTE QUALQUER TECLA PARA SAIR ----- ")
