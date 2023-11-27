from math import *

B = 0 #bloco
P = 0 #preenchimento
L = 0 #limite da tela

# os valores anteriores são iguais, para, caso queiramos colocar uma nova imagem para cada um dos elementos, não seja tão complicado
V = 1 #espaço vazio
EE = 2 #espinho virado para a esquerda
ED = 2 #espinho virado para a direita
EB = 2 #espinho virado para baixo
EC = 2 #espinho virado para cima
R = 6 #posição inicial do personagem
O = 7 #ponto de chegada
#M = 8 #moeda --> galinha
M = 8

MAPA_3 =[
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
    [ED,V,V,V,M,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,M,V,V,V,V,V,V,V,V,EE],
    [L,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,O,L],
    [L,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,B,V,V,B,B,B,B,B,B,L],
    [L,V,V,B,V,V,V,V,V,V,V,M,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,B,V,V,B,B,B,B,B,B,B,B,B,B,B,V,V,B,V,V,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,B,V,V,V,V,V,V,B,B,V,V,B,V,V,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,B,V,V,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,B,V,V,V,V,V,V,V,V,V,M,B,V,V,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,B,B,B,B,B,B,V,V,V,B,P,P,P,P,P,L],
    [L,V,V,R,V,V,V,M,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,P,L],
    [L,B,B,B,EC,EC,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,P,L],
    [P,P,P,P,P,P,P,P,B,EC,EC,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,P,P,P,P,L],
    [P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,L],
    [P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,L],
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L]]

#Legenda Bara localização
#O = linha de chegada
#V= VAZIO
#b = BlOco
#ec =  espinho Bara cima
#eB - espinho Bara baixo
#ed = espinho Bara direita


MAPA_2= [
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
    [L,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,B,V,V,V,V,V,O,L],
    [L,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,B,V,V,V,V,V,M,L],
    [L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,P,P,P,P,P,P,P,P,P,P,B,V,V,B,B,B,L],
    [ED,V,V,V,V,V,V,V,V,V,V,V,V,V,M,B,P,P,P,P,P,P,P,P,P,P,B,V,V,B,P,P,L],
    [L,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,P,P,P,P,P,P,B,V,V,B,P,P,L],
    [L,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,P,P,P,P,P,P,P,P,P,P,B,V,V,B,P,P,L],
    [L,V,V,B,B,B,B,B,EB,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,B,P,P,L],
    [L,V,V,B,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,P,P,L],
    [L,V,V,B,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,P,P,L],
    [L,V,V,B,V,V,V,B,V,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,B,V,V,B,P,P,L],
    [L,V,V,B,B,B,B,B,V,V,V,V,B,V,V,V,V,V,V,V,V,M,B,B,B,V,B,V,V,B,P,P,L],
    [L,V,V,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,B,V,V,B,P,P,L],
    [L,V,V,V,V,V,R,V,V,B,V,M,B,V,V,V,B,B,B,B,V,V,V,B,B,B,B,V,V,B,P,P,L],
    [L,B,B,B,B,B,B,B,B,P,B,B,B,V,V,V,B,B,B,B,V,V,V,B,B,B,B,V,V,B,P,P,L],
    [L,P,P,P,P,P,P,P,P,P,P,P,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,L],
    [L,L,L,L,L,L,L,L,L,L,L,L,L,EC,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L]]

MAPA_1=[
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
    [L,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L],
    [L,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L],
    [L,O,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,L],
    [L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,V,V,V,V,V,V,V,V,V,V,V,V,L],
    [L,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,B,V,V,V,V,V,V,V,V,V,V,V,V,L],
    [L,B,B,B,B,B,P,P,P,P,P,P,P,P,P,P,P,P,P,B,V,V,V,V,V,M,V,V,V,V,V,V,L],
    [ED,V,V,V,V,M,B,V,V,V,B,B,B,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,L],
    [L,V,V,V,V,V,B,V,V,B,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,B,P,P,P,P,L],
    [L,V,V,B,B,B,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,B,B,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,P,P,P,P,P,P,L],
    [L,V,V,B,V,V,V,V,V,B,V,V,V,V,V,V,V,V,V,B,V,V,V,V,V,B,P,P,P,P,P,P,L],
    [L,V,V,B,B,B,B,B,B,B,V,V,B,B,B,B,B,B,B,B,B,B,B,B,B,B,P,P,P,P,P,P,L],
    [L,V,V,V,V,V,V,V,V,B,V,V,V,V,V,V,V,B,P,P,P,P,P,P,P,P,P,P,P,P,P,P,L],
    [L,V,V,R,V,V,V,V,V,V,V,V,V,V,V,M,V,B,P,P,P,P,P,P,P,P,P,P,P,P,P,P,L],
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L]]






"""
MAPA_MODELO = [
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,L],
    [L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L]]
"""