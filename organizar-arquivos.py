import os 
import shutil

pasta = r"C:\Users\Administrator\Downloads"
arquivos = os.listdir(pasta)

for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho):
        extensao = arquivo.split(".")[-1].lower()

        if extensao in ["png", "jpg", "jpeg"]:
            destino = os.path.join(pasta, "Imagens")
        elif extensao in ["mp4", "mkv"]:
            destino = os.path.join(pasta, "Vídeos")
        else:
            destino = os.path.join(pasta, "Outros")
        if not os.path.exists(destino):
            os.mkdir(destino)
        
        novo_caminho = os.path.join(destino, arquivo)
        shutil.move(caminho, novo_caminho)

        print(f"Movendo: {arquivo} -> {destino}")