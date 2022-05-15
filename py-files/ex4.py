import cv2
import os
import sys
import os.path
import numpy as np

print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())


def antartida(bgr):
    """
        Não mude ou renomeie esta função
        deve receber uma imagem bgr e devolver o recorte da imagem da antartida
    """
    res = bgr.copy()
    # desenvolva sua resposta aqui

    return res


def canada(bgr):
    """
        Não mude ou renomeie esta função
        deve receber uma imagem bgr e devolver o recorte da imagem do canadá
    """
    res = bgr.copy()
    # desenvolva sua resposta aqui

    return res


if __name__ == "__main__":
    img = cv2.imread("imgs/ant_canada_250_160.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Faz o processamento
    antartida = antartida(img)
    canada = canada(img)
    cv2.imwrite("imgs/ex4_A_sol.png", antartida)
    cv2.imwrite("imgs/ex5_B_sol.png", canada)

    # Note que o OpenCV trabalha com BGR e não RGB
    cv2.imshow('entrada', img)
    cv2.imshow('antartida', antartida)
    cv2.imshow('canada', canada)

    cv2.waitKey(0)
