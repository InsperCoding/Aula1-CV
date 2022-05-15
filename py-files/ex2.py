import cv2
import os
import sys
import os.path
import numpy as np

print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())


def realca_caixa_vermelha(bgr):
    """
        Não mude ou renomeie esta função
        deve receber uma imagem bgr
        e fazer alguma filtragem / seleção de modo a obter uma imagem
        de saída grayscale
        em que somente os pixels da caixa estão brancos e todo o restante está vermelho
        Dica: Use mais de um canal, por exemplo R e B
    """
    res = bgr.copy()
    # desenvolva sua resposta aqui

    return res


if __name__ == "__main__":
    img = cv2.imread("imgs/cena_canto_sala.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Faz o processamento
    saida = realca_caixa_vermelha(img)
    cv2.imwrite("imgs/ex2_sol.png", saida)

    # Note que o OpenCV trabalha com BGR e não RGB
    cv2.imshow('entrada', img)
    cv2.imshow('saida', saida)

    cv2.waitKey(0)
