from math import *

B = 0
V = 1
E = 2

MABA_3 =[
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [E,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,E]
    [B,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,O,B]
    [B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,V,V,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,B,B,B,B,B,B,B,B,B,B,B,V,V,B,V,V,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,B,V,V,V,V,V,V,B,B,V,V,B,V,V,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B,V,V,V,B,B,B,B,B,B,B]
    [B,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B]
    [B,B,B,B,E,E,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,E,E,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]]

#Legenda Bara localização
#V= VAZIO
#b = BlOco
#ec =  esBinho Bara cima
#eB - esBinho Bara baixo
#ed = esBinho Bara direita


MABA_2= [
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,O,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,B,B]
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,V,V,V,B,B,B,B]
    [E,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,B,B]
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,B,B]
    [B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,B,B]
    [B,V,V,B,B,B,B,B,E,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,B,B]
    [B,V,V,B,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,B,B,B]
    [B,V,V,B,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,B,B,B]
    [B,V,V,B,V,V,V,B,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,V,V,B,B,B,B]
    [B,V,V,B,B,B,B,B,V,V,V,V,B,V,V,V,V,V,V,V,V,B,B,B,V,V,B,V,V,B,B,B,B]
    [B,V,V,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,B,B,B]
    [B,V,V,V,V,V,V,V,V,B,V,B,B,V,V,V,B,B,B,B,V,V,V,B,B,B,B,V,V,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,B,B,B,B,V,V,V,B,B,B,B,V,V,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,E,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]]

MABA_1=[
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B]
    [B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B]
    [B,O,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,B,V,V,V,V,V,V,B]
    [E,V,V,V,V,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,V,V,V,B,B,B,B,B,B,B,B,B,B]
    [B,V,V,V,V,V,B,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B]
    [B,V,V,B,B,B,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,B,B,B,B,B]
    [B,V,V,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]]

"""
MABA_MODEBO = [
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,B]
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]]
"""