import cv2
import os
import sys
import os.path
import numpy as np

print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())


def equaliza(gray):
    """
        Não mude ou renomeie esta função
        deve receber uma imagem e devolver uma imagem nova com o histograma equalizado
    """
    res = gray.copy()
    # desenvolva sua resposta aqui

    return res


if __name__ == "__main__":
    img = cv2.imread("imgs/RinTinTin.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Faz o processamento
    saida = equaliza(gray)
    cv2.imwrite("imgs/ex1_sol.png", saida)

    # Note que o OpenCV trabalha com BGR e não RGB
    cv2.imshow('entrada', img)
    cv2.imshow('saida', saida)

    cv2.waitKey(0)
