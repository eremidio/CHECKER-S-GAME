#Vamos criar um jogo de damas
#O jogo usará apenas linhas de comando e poderá ser invocado do teminal do computador
#o jogo não terá uma interface gráfica e todos os seus elementos usarão caracteres do teclado do computador

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#0: Cabeçalho e bibliotecas usadas na construnção do jogo
#0.1: importando bibliotecas
import random

#0.2:cabeçalho do jogo

print('Bem vindo ao jogo de damas. \n Esperamos que você se divirta com este jogo.\n Vamos jogar este jogo num tabuleiro 8x8 que apresentamos abaixo.')

#Gerando a malha quadrada 8x8 que irá alocar as peças no tabuleiro de damas
print('+------+------+------+------+------+------+------+------+           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |  8        ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('+------+------+------+------+------+------+------+------+           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||  7        ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('+------+------+------+------+------+------+------+------+           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |  6        ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('+------+------+------+------+------+------+------+------+           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||  5        ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('+------+------+------+------+------+------+------+------+   eixo x  ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |  4        ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('+------+------+------+------+------+------+------+------+           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||  3        ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('+------+------+------+------+------+------+------+------+           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('||||||||      ||||||||      ||||||||      ||||||||      |  2        ')
print('||||||||      ||||||||      ||||||||      ||||||||      |           ')
print('+------+------+------+------+------+------+------+------+           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||  1        ')
print('|      ||||||||      ||||||||      ||||||||      ||||||||           ')
print('+------+------+------+------+------+------+------+------+           ')
print('    1      2      3      4      5      6      7      8              ')
print('                        eixo y                                  \n\n') 

print('As casas contendo um 000000 não estão acessíveis durante o jogo. \n')

print('Para você executar um movimento ser requerido que você use o teclado para especificar as coordenadas das casas de inicial e final de uma peça.\n A primeira coordenada refere-se ao eixo x mostrado na imagem acima e a segunda coordenada refere-se ao eixo y mostrado na imagem acima.\n')

print('Durante o jogo usaremos a seguinte notação para as peças:\n PB: pedra branca, PP: pedra preta, DB: dama branca, DP: dama preta.\n')

print('No jogo de damas as peças comuns podem apenas avançar em direção a outra extremidade do tabuleiro, ao passo que as damas tem liberdade total para fazer movimentos legais.\nCaso algum jogador fique sem movimento legal, será autorizado que ele realize um movimento com uma peça comum de retrocesso no tabuleiro de damas.\n')

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#1: Construindo o tabuleiro

'''Vamos definir o tabuleiro do jogo para alocar peças do jogo de damas. usaremos Uma lista com 8 listas de 8 elementos'''
 
tabuleiro:list=[['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'],]


'''Módulo de teste do tabuleiro acima, use  um # após o teste'''
#print(tabuleiro1[0][0])
#print(tabuleiro1[1][1])
#print(tabuleiro1[7][7])

#Vamos definir uma função que permite posicionar as peças no tabuleiro'''
#Vamos definir uma função que permite posicionar as peças no tabuleiro'''
def posicao(tabuleiro:list):
 '''Função que serve para posicionar as peças de xadrez no tabuleiro atualizando seu status'''
 print('+------+------+------+------+------+------+------+------+  ')
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('|00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  | 8'.format(tabuleiro[7][0],tabuleiro[7][1],tabuleiro[7][2],tabuleiro[7][3],tabuleiro[7][4],tabuleiro[7][5],tabuleiro[7][6], tabuleiro[7][7]))
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00| 7'.format(tabuleiro[6][0],tabuleiro[6][1],tabuleiro[6][2],tabuleiro[6][3],tabuleiro[6][4],tabuleiro[6][5],tabuleiro[6][6], tabuleiro[6][7]))
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('|00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  | 6'.format(tabuleiro[5][0],tabuleiro[5][1],tabuleiro[5][2],tabuleiro[5][3],tabuleiro[5][4],tabuleiro[5][5],tabuleiro[5][6], tabuleiro[5][7]))
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00| 5'.format(tabuleiro[4][0],tabuleiro[4][1],tabuleiro[4][2],tabuleiro[4][3],tabuleiro[4][4],tabuleiro[4][5],tabuleiro[4][6], tabuleiro[4][7]))
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('+------+------+------+------+------+------+------+------+   eixo x')
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('|00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  | 4'.format(tabuleiro[3][0],tabuleiro[3][1],tabuleiro[3][2],tabuleiro[3][3],tabuleiro[3][4],tabuleiro[3][5],tabuleiro[3][6], tabuleiro[3][7]))
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00| 3'.format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2],tabuleiro[2][3],tabuleiro[2][4],tabuleiro[2][5],tabuleiro[2][6], tabuleiro[2][7]))
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('|00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  | 2'.format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2],tabuleiro[1][3],tabuleiro[1][4],tabuleiro[1][5],tabuleiro[1][6], tabuleiro[1][7]))
 print('|000000|      |000000|      |000000|      |000000|      |  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00|  {}  |00{}00| 1'.format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2],tabuleiro[0][3],tabuleiro[0][4],tabuleiro[0][5],tabuleiro[0][6], tabuleiro[0][7]))
 print('|      |000000|      |000000|      |000000|      |000000|  ')
 print('+------+------+------+------+------+------+------+------+  ')
 print('    1      2      3      4      5      6      7      8     ')
 print('                           eixo y                        \n')
'''Testando a função posição. Use um # após o teste'''
#posicao(tabuleiro)



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#2: Ajustando o tabuleiro na posição inicial

tabuleiro:list=[['PB','00','PB','00','PB','00','PB','00'], ['00','PB','00','PB','00','PB','00','PB'], ['PB','00','PB','00','PB','00','PB','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','PP','00','PP','00','PP','00','PP'], ['PP','00','PP','00','PP','00','PP','00'], ['00','PP','00','PP','00','PP','00','PP'],]

posicao(tabuleiro)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#3: Realizando um movimento de peça no tabuleiro para uma peça pedra

#Função que valida o movimento de uma pedra em caso de não haver captura
def validar_lance_pedra(a:int, b:int, c:int, d:int)->bool:
 '''Uma função que valida o movimento de pedra sem captura'''
 if(a-1<=7 and b-1<=7 and c-1<=7 and d-1<=7 and (a+b)%2==0 and (c+d)%2==0):
  return True
 else:
  return False

#Função que executa o movimento de uma pedra em caso de não haver captura
def mover_pedra(tabuleiro:list)->list:
 '''Função que executa o movimento de uma pedra sem captura'''
 numero1=int(input('Digite a primeira coordenada da casa inicial da pedra:'))
 numero2=int(input('Digite a segunda coordenada da casa inicial da pedra:'))
 numero3=int(input('Digite a primeira coordenada da casa final da pedra:'))
 numero4=int(input('Digite a segunda coordenada da casa final da pedra:'))
 if (validar_lance_pedra(numero1, numero2, numero3, numero4)==True and abs(numero1-numero3)==1 and abs(numero2-numero4)==1):
  if(tabuleiro[numero1-1][numero2-1]=='PB'):
   if(tabuleiro[numero3-1][numero4-1]=='--'):
    tabuleiro[numero1-1][numero2-1]='--'
    tabuleiro[numero3-1][numero4-1]='PB'
  if(tabuleiro[numero1-1][numero2-1]=='PP'):
   if(tabuleiro[numero3-1][numero4-1]=='--'):
    tabuleiro[numero1-1][numero2-1]='--'
    tabuleiro[numero3-1][numero4-1]='PP'
 else:
  print('Escolha outra casa.\n Perdeu a vez.\n') 
 return tabuleiro
 

'''Módulo de teste da função que executa movimento de uma pedra, use um # após o  teste'''
#mover_pedra(tabuleiro)
#posicao(tabuleiro) 

#Funções de capturas de pedras

def validar_captura_pedra_brancas(tabuleiro:list, a:int, b:int)->bool:
 '''Função que valida a captura de uma pedra ou dama do aversário no jogo usando as coordenadas inseridas pelo usuário'''
 #Pedra capturando pedra
 if (a-1<=7 and b-1<=7 and a-2<=7 and b-2<=7 and a-3<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a-2][b-2]=='PP' and tabuleiro[a-3][b-3]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a-2<=7 and b<=7 and a-3<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a-2][b]=='PP' and tabuleiro[a-3][b+1]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a<=7 and b<=7 and a+1<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a][b]=='PP' and tabuleiro[a+1][b+1]=='--'):
   return True   
 if (a-1<=7 and b-1<=7 and a<=7 and b-2<=7 and a+1<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a][b-2]=='PP' and tabuleiro[a+1][b-3]=='--'):
   return True   
 #Pedra capturando damas
 if (a-1<=7 and b-1<=7 and a-2<=7 and b-2<=7 and a-3<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a-2][b-2]=='DP' and tabuleiro[a-3][b-3]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a-2<=7 and b<=7 and a-3<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a-2][b]=='DP' and tabuleiro[a-3][b+1]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a<=7 and b<=7 and a+1<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a][b]=='DP' and tabuleiro[a+1][b+1]=='--'):
   return True   
 if (a-1<=7 and b-1<=7 and a<=7 and b-2<=7 and a+1<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PB' and tabuleiro[a][b-2]=='DP' and tabuleiro[a+1][b-3]=='--'):
   return True 
 else:
  return False

def validar_captura_pedra_pretas(tabuleiro:list, a:int, b:int)->bool:
 '''Função que valida a captura de uma pedra ou dama do aversário no jogo usando as coordenadas inseridas pelo usuário'''
 #Pedra capturando pedra
 if (a-1<=7 and b-1<=7 and a-2<=7 and b-2<=7 and a-3<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a-2][b-2]=='PB' and tabuleiro[a-3][b-3]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a-2<=7 and b<=7 and a-3<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a-2][b]=='PB' and tabuleiro[a-3][b+1]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a<=7 and b<=7 and a+1<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a][b]=='PB' and tabuleiro[a+1][b+1]=='--'):
   return True   
 if (a-1<=7 and b-1<=7 and a<=7 and b-2<=7 and a+1<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a][b-2]=='PB' and tabuleiro[a+1][b-3]=='--'):
   return True   
 #Pedra capturando damas
 if (a-1<=7 and b-1<=7 and a-2<=7 and b-2<=7 and a-3<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a-2][b-2]=='DB' and tabuleiro[a-3][b-3]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a-2<=7 and b<=7 and a-3<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a-2][b]=='DB' and tabuleiro[a-3][b+1]=='--'):
   return True
 if (a-1<=7 and b-1<=7 and a<=7 and b<=7 and a+1<=7 and b+1<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a][b]=='DB' and tabuleiro[a+1][b+1]=='--'):
   return True   
 if (a-1<=7 and b-1<=7 and a<=7 and b-2<=7 and a+1<=7 and b-3<=7):
  if (tabuleiro[a-1][b-1]=='PP' and tabuleiro[a][b-2]=='DB' and tabuleiro[a+1][b-3]=='--'):
   return True 
 else:
  return False


def assinalar_captura_pedra(tabuleiro:list)->str:
 '''Uma função que assinala ao jogador se há ou não uma possibilidade de captura'''
 #Variável de contagem
 contador:int=0
 for i in range(8):
  for j in range(8):
   if(validar_captura_pedra_brancas(tabuleiro, i, j)==True or validar_captura_pedra_pretas(tabuleiro, i, j)==True):
     contador=contador+1
 if(contador!=0):
  print('Há uma captura para ser realizada. Atenção jogador.\n')
   

def capturar_pedra_brancas(tabuleiro:list)->list:
 '''Função de captura de uma pedra ou dama por uma pedra no tabuleiro de damas'''
 numero1=int(input('Digite a primeira coordenada da casa inicial da pedra:'))
 numero2=int(input('Digite a segunda coordenada da casa inicial da pedra:'))
 numero3=int(input('Digite a primeira coordenada da casa final da pedra:'))
 numero4=int(input('Digite a segunda coordenada da casa final da pedra:'))
 if validar_captura_pedra_brancas(tabuleiro, numero1, numero2)==True:
  tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1] 
  tabuleiro[numero1-1][numero2-1]='--'
  tabuleiro[int(((numero1+numero3)/2)-1)][int(((numero2+numero4)/2)-1)]='--'
  print('Uma peça foi capturada.')
 return tabuleiro

def capturar_pedra_pretas(tabuleiro:list)->list:
 '''Função de captura de uma pedra ou dama por uma pedra no tabuleiro de damas'''
 numero1=int(input('Digite a primeira coordenada da casa inicial da pedra:'))
 numero2=int(input('Digite a segunda coordenada da casa inicial da pedra:'))
 numero3=int(input('Digite a primeira coordenada da casa final da pedra:'))
 numero4=int(input('Digite a segunda coordenada da casa final da pedra:'))
 if validar_captura_pedra_pretas(tabuleiro, numero1, numero2)==True:
  tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1] 
  tabuleiro[numero1-1][numero2-1]='--'
  tabuleiro[int(((numero1+numero3)/2)-1)][int(((numero2+numero4)/2)-1)]='--'
  print('Uma peça foi capturada.')
 return tabuleiro

'''Módulo de teste das funções de captura de peças por pedras comuns, use um # após os testes'''
#mover_pedra(tabuleiro)
#posicao(tabuleiro) 
#mover_pedra(tabuleiro)
#posicao(tabuleiro) 
#assinalar_captura_pedra(tabuleiro)
#capturar_pedra_brancas(tabuleiro)
#posicao(tabuleiro)
#assinalar_captura_pedra(tabuleiro)
#capturar_pedra_pretas(tabuleiro)
#posicao(tabuleiro)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#4: Função que define a promoção de uma pedra comum em dama
def validar_promocao(tabuleiro:list)->bool:
 '''Função que valida a promoção de uma pedra'''
 if(tabuleiro[7][1]=='PB' or tabuleiro[7][3]=='PB' or tabuleiro[7][5]=='PB' or tabuleiro[7][7]=='PB'):
  print('Uma pedra das brancas será promovida a dama.\n')
  return True
 if(tabuleiro[0][0]=='PP' or tabuleiro[0][2]=='PP' or tabuleiro[0][4]=='PP' or tabuleiro[0][6]=='PP'):
  print('Uma pedra das pretas será promovida a dama.\n')
  return True

def promover_pedra(tabuleiro:list)->list:
 '''Função que promove uma pedra a dama'''
 if(validar_promocao(tabuleiro)==True):
  if(tabuleiro[7][1]=='PB'):
   tabuleiro[7][1]='DB'
  if(tabuleiro[7][3]=='PB'):
   tabuleiro[7][3]='DB'
  if(tabuleiro[7][5]=='PB'):
   tabuleiro[7][5]='DB'
  if(tabuleiro[7][7]=='PB'):
   tabuleiro[7][7]='DB'
  if(tabuleiro[0][0]=='PP'):
   tabuleiro[0][0]='DP'
  if(tabuleiro[0][2]=='PP'):
   tabuleiro[0][2]='DP'
  if(tabuleiro[0][4]=='PP'):
   tabuleiro[0][4]='DP'
  if(tabuleiro[0][6]=='PP'):
   tabuleiro[0][6]='DP'
 return tabuleiro


'''Módulo para teste de promoção de damas no tabuleiro, use um # após os testes'''
#tabuleiro:list=[['--','00','--','00','--','00','--','00'], ['00','PP','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','PB','00'], ['00','--','00','--','00','--','00','--'],]
#posicao(tabuleiro)
#mover_pedra(tabuleiro)
#posicao(tabuleiro)
#validar_promocao(tabuleiro)
#promover_pedra(tabuleiro)
#posicao(tabuleiro)
#mover_pedra(tabuleiro)
#posicao(tabuleiro)
#validar_promocao(tabuleiro)
#promover_pedra(tabuleiro)
#posicao(tabuleiro)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#5: Realizando a movimentação de uma dama no tabuleiro

#Função que valida a movimentação de uma dama em caso de não haver capturas de peças adversárias
def validar_lance_dama(tabuleiro:list, a:int, b:int, c:int, d:int)->bool:
 '''Função que valida o movimento de uma dama'''
 #Variável que define o salto da dama
 salto_dama=abs(a-c)
 if(tabuleiro[a-1][b-1]=='DP' or tabuleiro[a-1][b-1]=='DP'):
  for i in range (salto_dama+1):
   if (tabuleiro[a-1-i][b-1-i]=='--'):
    return True
   if (tabuleiro[a-1-i][b-1+i]=='--'):
    return True
   if (tabuleiro[a-1+i][b-1+i]=='--'):
    return True
   if (tabuleiro[a-1+i][b-1-i]=='--'):
    return True
 else:
  return False

#Função que executa o movimento de uma dama em caso de não haver captura 
def mover_dama(tabuleiro:list)->list:
 '''Função que movimenta uma dama sem captura'''
 numero1=int(input('Digite a primeira coordenada da casa inicial da pedra:'))
 numero2=int(input('Digite a segunda coordenada da casa inicial da pedra:'))
 numero3=int(input('Digite a primeira coordenada da casa final da pedra:'))
 numero4=int(input('Digite a segunda coordenada da casa final da pedra:'))
 if(validar_lance_dama(tabuleiro, numero1, numero2, numero3, numero4)==True):
  if(tabuleiro[numero1-1][numero2-1]=='DB'):
   if(tabuleiro[numero3-1][numero4-1]=='--'):
    tabuleiro[numero1-1][numero2-1]='--'
    tabuleiro[numero3-1][numero4-1]='DB'
  if(tabuleiro[numero1-1][numero2-1]=='DP'):
   if(tabuleiro[numero3-1][numero4-1]=='--'):
    tabuleiro[numero1-1][numero2-1]='--'
    tabuleiro[numero3-1][numero4-1]='DP'
 else:
  print('Escolha outra casa.\n Perdeu a vez.\n') 
 return tabuleiro

#Função que valida a captura de uma peça adversária pela dama
def validar_captura_dama_brancas(tabuleiro:list, a:int, b:int)->bool:
 '''Função que valida a captura de uma peça do adversário com a dama''' 
 #Validando captura para damas brancas
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DB'):
  for i in range(7):
   if((a+i)<=7 and (b+i)<=7):
    if(tabuleiro[a-1+i][b-1+i]=='PP' or tabuleiro[a-1+i][b-1+i]=='DP'):
     if(tabuleiro[a+i][b+i]=='--'): 
      return True
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DB'):
  for i in range(7):
   if((a-i-1)>=0 and (b-1-i)>=0):
    if(tabuleiro[a-i][b-i]=='PP' or tabuleiro[a-i][b-i]=='DP'):
     if(tabuleiro[a-i-1][b-i-1]=='--'): 
      return True
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DB'):
  for i in range(7):
   if((b+i-1)<=7 and (a-i-1)>=0):
    if(tabuleiro[a-i][b+i-2]=='PP' or tabuleiro[a-i][b+i-2]=='DP'):
     if(tabuleiro[a-i-1][b-1+i]=='--'): 
      return True
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DB'):
  for i in range(7):
   if((a+i-1)<=7 and (b-i-1)>=0):
    if(tabuleiro[a+i-2][b-i]=='PP' or tabuleiro[a+i-2][b-i]=='DP'):
     if(tabuleiro[a+i-1][b-i-1]=='--'): 
      return True

def validar_captura_dama_pretas(tabuleiro:list, a:int, b:int)->bool:
 '''Função que valida a captura de uma peça do adversário com a dama''' 
 #Validando captura para damas pretas
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DP'):
  for i in range(7):
   if((a+i)<=7 and (b+i)<=7):
    if(tabuleiro[a-1+i][b-1+i]=='PB' or tabuleiro[a-1+i][b-1+i]=='DB'):
     if(tabuleiro[a+i][b+i]=='--'): 
      return True
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DP'):
  for i in range(7):
   if((a-i-1)>=0 and (b-1-i)>=0):
    if(tabuleiro[a-i][b-i]=='PB' or tabuleiro[a-i][b-i]=='DB'):
     if(tabuleiro[a-i-1][b-i-1]=='--'): 
      return True
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DP'):
  for i in range(7):
   if((b+i-1)<=7 and (a-i-1)>=0):
    if(tabuleiro[a-i][b+i-2]=='PB' or tabuleiro[a-i][b+i-2]=='DB'):
     if(tabuleiro[a-i-1][b-1+i]=='--'): 
      return True
 if((a-1)<=7 and (b-1)<=7 and tabuleiro[a-1][b-1]=='DP'):
  for i in range(7):
   if((a+i-1)<=7 and (b-i-1)>=0):
    if(tabuleiro[a+i-2][b-i]=='PB' or tabuleiro[a+i-2][b-i]=='DB'):
     if(tabuleiro[a+i-1][b-i-1]=='--'): 
      return True

#Função que assinala uma captura de pedra por uma dama

def assinalar_captura_dama(tabuleiro:list)->str:
 '''Uma função que assinala ao jogador se há ou não uma possibilidade de captura'''
 #Variável de contagem
 contador:int=0
 for i in range(8):
  for j in range(8):
   if(validar_captura_dama_brancas(tabuleiro, i, j)==True or validar_captura_dama_pretas(tabuleiro, i, j)==True):
    contador=contador+1
 if(contador!=0):
  print('Há uma captura para ser realizada. Atenção jogador.\n')
   
#Função que realiza uma captura de pedra por uma dama
def capturar_dama_brancas(tabuleiro:list)->list:
 '''Função de captura de uma pedra por outra pedra no tabuleiro de damas'''
 numero1=int(input('Digite a primeira coordenada da casa inicial da pedra:'))
 numero2=int(input('Digite a segunda coordenada da casa inicial da pedra:'))
 numero3=int(input('Digite a primeira coordenada da casa final da pedra:'))
 numero4=int(input('Digite a segunda coordenada da casa final da pedra:'))
 salto_dama=abs(numero3-numero1)
 if validar_captura_dama_brancas(tabuleiro, numero1, numero2)==True:
  if((numero3-numero1)>0 and (numero4-numero2)>0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1+i][numero2-1+i]='--'
  if((numero3-numero1)<0 and (numero4-numero2)<0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1-i][numero2-1-i]='--'
  if ((numero3-numero1)<0 and (numero4-numero2)>0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1-i][numero2-1+i]='--'
  if ((numero3-numero1)>0 and (numero4-numero2)<0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1+i][numero2-1-i]='--'
 print('Uma peça foi capturada.')
 return tabuleiro

def capturar_dama_pretas(tabuleiro:list)->list:
 '''Função de captura de uma pedra por outra pedra no tabuleiro de damas'''
 numero1=int(input('Digite a primeira coordenada da casa inicial da pedra:'))
 numero2=int(input('Digite a segunda coordenada da casa inicial da pedra:'))
 numero3=int(input('Digite a primeira coordenada da casa final da pedra:'))
 numero4=int(input('Digite a segunda coordenada da casa final da pedra:'))
 salto_dama=abs(numero3-numero1)
 if validar_captura_dama_pretas(tabuleiro, numero1, numero2)==True:
  if((numero3-numero1)>0 and (numero4-numero2)>0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1+i][numero2-1+i]='--'
  if((numero3-numero1)<0 and (numero4-numero2)<0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1-i][numero2-1-i]='--'
  if ((numero3-numero1)<0 and (numero4-numero2)>0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1-i][numero2-1+i]='--'
  if ((numero3-numero1)>0 and (numero4-numero2)<0):
   tabuleiro[numero3-1][numero4-1]=tabuleiro[numero1-1][numero2-1]
   tabuleiro[numero1-1][numero2-1]='--'
   for i in range(salto_dama):
    tabuleiro[numero1-1+i][numero2-1-i]='--'
 print('Uma peça foi capturada.')
 return tabuleiro
'''Módulo de teste do movimento de damas no tabuleiro, use um # após os testes'''
#tabuleiro:list=[['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'], ['--','00','--','00','--','00','DP','00'], ['00','--','00','DB','00','--','00','--'], ['--','00','--','00','--','00','--','00'], ['00','--','00','--','00','--','00','--'],]
#posicao(tabuleiro)
#mover_dama(tabuleiro)
#posicao(tabuleiro)
#assinalar_captura_dama(tabuleiro)
#capturar_dama_brancas(tabuleiro)
#capturar_dama_pretas(tabuleiro)
#posicao(tabuleiro)


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#6: Definindo variáveis de contagem de peças e de contagem de rodadas da partida

#Vamos definir duas variáveis de contagem de peças pretas e brancas que serão usadas para determinar se há algum vencedor
n_pecas_brancas:int=0
n_pecas_pretas:int=0
n_rodadas:int=0
#Atualizando as variáveis de contagem
for i in range(8):
 for j in range(8):
  if(tabuleiro[i][j]=='DB' or tabuleiro[i][j]=='PB'):
   n_pecas_brancas=n_pecas_brancas+1
  if(tabuleiro[i][j]=='DP' or tabuleiro[i][j]=='PP'):
   n_pecas_pretas=n_pecas_pretas+1

'''Módulo de testes das variáveis de contagem de peças, use um # após os teste'''
#print(n_pecas_brancas)
#print(n_pecas_pretas)



#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#7:Funções utéis durante o jogo 

#Função que determina se há ou não damas no tabuleiro. Esta função será usada para decidir se durante um jogo o jogador moverá uma dama ou uma pedra comum

def existe_damas_brancas(tabuleiro:list)->bool:
 '''Função que determina se há ou não uma dama no tabuleiro'''
 #Variável de contagem
 contador:int=0
 #esquadrinando o tabuleiro
 for i in range(8):
  for j in range(8):
   if(tabuleiro[i][j]=='DB'):
     contador=contador+1
 if(contador>0):
  return True
 elif(contador==0):
  return False

def existe_damas_pretas(tabuleiro:list)->bool:
 '''Função que determina se há ou não uma dama no tabuleiro'''
 #Variável de contagem
 contador:int=0
 #esquadrinando o tabuleiro
 for i in range(8):
  for j in range(8):
   if(tabuleiro[i][j]=='DP'):
     contador=contador+1
 if(contador>0):
  return True
 elif(contador==0):
  return False

#Função que determina a vitória em caso de todas as peças de um jogador serem eliminadas do tabuleiro
def vitoria(n_pecas_pretas:int, n_pecas_brancas:int)->bool:
 '''Função que dá vitória a um dos jogadores'''
 if(n_pecas_pretas==0 and n_pecas_brancas!=0):
  print('O jogador de brancas venceu!!!\n Parabéns.\n')
  return True
 elif(n_pecas_pretas!=0 and n_pecas_brancas==0):
  print('O jogador de pretas venceu!!!\n Parabéns.\n')
  return True
 else:
  return False

#Função que define a ação a ser realizada no jogo
def gameplay_brancas(tabuleiro:list)->str:
 '''Função que define o movimento a ser realizado na partida'''
 acao:str=' '
 contador:int=0 #Captura de pedras
 contador2:int=0 #Captura de damas
 for i in range(8):
  for j in range(8):
   if(validar_captura_pedra_brancas(tabuleiro, i, j)==True):
    contador=contador+1
   if(validar_captura_dama_brancas(tabuleiro, i, j)==True):
    contador2=contador2+1
 if(contador!=0 and contador2==0):
  acao='capturar_pedra'
 if(contador!=0 and contador2!=0):
  acao='capturar' #pedra ou dama (decisão do usuário)
 elif(contador==0 and contador2==0):
  acao='mover'
 return acao

def gameplay_pretas(tabuleiro:list)->str:
 '''Função que define o movimento a ser realizado na partida'''
 acao:str=' '
 contador:int=0 #Captura de pedras
 contador2:int=0 #Captura de damas
 for i in range(8):
  for j in range(8):
   if(validar_captura_pedra_pretas(tabuleiro, i, j)==True):
    contador=contador+1
   if(validar_captura_dama_pretas(tabuleiro, i, j)==True):
    contador2=contador2+1
 if(contador!=0 and contador2==0):
  acao='capturar_pedra'
 if(contador!=0 and contador2!=0):
  acao='capturar' #pedra ou dama (decisão do usuário)
 elif(contador==0 and contador2==0):
  acao='mover'
 return acao

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#8: Desenvolvimento da partida

#Mensagem a ser exibida com as instruções do jogo
print('Preparados?!\nO jogador de brancas irá iniciar a partida.\n')

#Rodada inicial brancas fazem o primeiro movimento e pretas fazem o segundo movimento
print('Jogador de brancas faça a sua jogada.\n')
mover_pedra(tabuleiro)
posicao(tabuleiro)
print('Jogador de pretas faça a sua jogada.\n')
mover_pedra(tabuleiro)
posicao(tabuleiro)
n_rodadas=1 #Atualizando o status do número de rodadas
print(n_rodadas)


#A partir deste lance pode já haver capturas de pedras então usaremos um loop While que irá definir o rumo do jogo. Ele irá para quando um dos jogadores não tiver mais peças no tabuleiro de damas. Introduziremos durante o jogo uma condição extra que definirá o fim do jogo quando não houver movimentos legais de peças.

while(vitoria(n_pecas_pretas, n_pecas_brancas)==False):
 '''Pausa forçada para testar as demais funções do programa, use um # para que jogo rode normalmente'''
 #break
  
 #Movimentos alternados de brancas e negras
 #Variáveis lógicas para determina a execução dos lances
 brancas:bool=True
 pretas:bool=True

 #Jogada das brancas
 while(brancas==True):
  print('Brancas jogam agora.\n')
  if(existe_damas_brancas(tabuleiro)==False and gameplay_brancas(tabuleiro)=='capturar_pedra'):
   while(gameplay_brancas(tabuleiro)=='capturar_pedra'):
    #caso nao haja damas no tabuleiro o jogador de brancas devem capturar peça se houver capturas válidas
    assinalar_captura_pedra(tabuleiro)
    capturar_pedra_brancas(tabuleiro)
    posicao(tabuleiro)
    brancas=False
    gameplay_brancas(tabuleiro)
   if(validar_promocao(tabuleiro)==True):
    validar_promocao(tabuleiro)
    promover_pedra(tabuleiro)
    posicao(tabuleiro)
    brancas=False
   break
  if(existe_damas_brancas(tabuleiro)==False and gameplay_brancas(tabuleiro)=='mover'):
   mover_pedra(tabuleiro)
   posicao(tabuleiro)
   brancas=False
   if(validar_promocao(tabuleiro)==True):
    validar_promocao(tabuleiro)
    promover_pedra(tabuleiro)
    posicao(tabuleiro)
    brancas=False
  #Caso haja damas no tabuleiro o jogador de brancas tem de tomar uma decisão de qual peça mover
  if(existe_damas_brancas(tabuleiro)==True):
   escolha:str=str(input('Digite "p" para mover uma pedra ou "d" para mover uma dama:\n'))
   if(escolha=='p' and gameplay_brancas(tabuleiro)=='capturar'):
    while(gameplay_brancas(tabuleiro)=='capturar'):
     #caso nao haja damas no tabuleiro o jogador de brancas devem capturar peça se houver capturas válidas
     assinalar_captura_pedra(tabuleiro)
     capturar_pedra_brancas(tabuleiro)
     posicao(tabuleiro)
     brancas=False
     gameplay_brancas(tabuleiro)  
    if(validar_promocao(tabuleiro)==True):
     validar_promocao(tabuleiro)
     promover_pedra(tabuleiro)
     posicao(tabuleiro)
     brancas=False
    break
   if(escolha=='p' and gameplay_brancas(tabuleiro)=='mover'):
    mover_pedra(tabuleiro)
    posicao(tabuleiro)
    brancas=False
    if(validar_promocao(tabuleiro)==True):
     validar_promocao(tabuleiro)
     promover_pedra(tabuleiro)
     posicao(tabuleiro)
     brancas=False
   #Caso o jogador queira mover uma dama, primeiro checa-se há caturas a serem feitas
   if(escolha=='d' and gameplay_brancas(tabuleiro)=='capturar'):
    while(gameplay(tabuleiro)=='capturar'):
     assinalar_captura_dama(tabuleiro)
     capturar_dama_brancas(tabuleiro)
     posicao(tabuleiro)
     brancas=False
     gameplay_brancas(tabuleiro)
    break
   if(escolha=='d' and gameplay_brancas(tabuleiro)=='mover'):
    mover_dama(tabuleiro)
    posicao(tabuleiro)
    brancas=False
 
 #Atualizando as variáveis de contagem após o movimento das brancas
 n_pecas_brancas=0
 n_pecas_pretas=0
 for i in range(8):
  for j in range(8):
   if(tabuleiro[i][j]=='DB' or tabuleiro[i][j]=='PB'):
    n_pecas_brancas=n_pecas_brancas+1
   if(tabuleiro[i][j]=='DP' or tabuleiro[i][j]=='PP'):
    n_pecas_pretas=n_pecas_pretas+1 


 #Se as brancas capturarem todas as peças das pretas o jogo termina antes das pretas fazerem o seu lance
 if(vitoria(n_pecas_pretas, n_pecas_brancas)==True):
  break

 #Jogada das pretas
 while(pretas==True):
  print('Pretas jogam agora.\n')
  if(existe_damas_pretas(tabuleiro)==False and gameplay_pretas(tabuleiro)=='capturar_pedra'):
   while(gameplay_pretas(tabuleiro)=='capturar_pedra'):
    #caso nao haja damas no tabuleiro o jogador de brancas devem capturar peça se houver capturas válidas
    assinalar_captura_pedra(tabuleiro)
    capturar_pedra_pretas(tabuleiro)
    posicao(tabuleiro)
    pretas=False
    gameplay_pretas(tabuleiro)
   if(validar_promocao(tabuleiro)==True):
    validar_promocao(tabuleiro)
    promover_pedra(tabuleiro)
    posicao(tabuleiro)
    pretas=False
   break
  if(existe_damas_pretas(tabuleiro)==False and gameplay_pretas(tabuleiro)=='mover'):
   mover_pedra(tabuleiro)
   posicao(tabuleiro)
   pretas=False
   if(validar_promocao(tabuleiro)==True):
    validar_promocao(tabuleiro)
    promover_pedra(tabuleiro)
    posicao(tabuleiro)
    pretas=False
  #Caso haja damas no tabuleiro o jogador de pretas tem de tomar uma decisão de qual peça mover
  if(existe_damas_pretas(tabuleiro)==True):
   escolha:str=str(input('Digite "p" para mover uma pedra ou "d" para mover uma dama:\n'))
   if(escolha=='p' and gameplay_pretas(tabuleiro)=='capturar'):
    while(gameplay_pretas(tabuleiro)=='capturar'):
     #caso nao haja damas no tabuleiro o jogador de pretas devem capturar peça se houver capturas válidas
     assinalar_captura_pedra(tabuleiro)
     capturar_pedra_pretas(tabuleiro)
     posicao(tabuleiro)
     pretas=False
     gameplay_pretas(tabuleiro)
    if(validar_promocao(tabuleiro)==True):
     validar_promocao(tabuleiro)
     promover_pedra(tabuleiro)
     posicao(tabuleiro)
     pretas=False
    break
   if(escolha=='p' and gameplay_pretas(tabuleiro)=='mover'):
    mover_pedra(tabuleiro)
    posicao(tabuleiro)
    pretas=False
    if(validar_promocao(tabuleiro)==True):
     validar_promocao(tabuleiro)
     promover_pedra(tabuleiro)
     posicao(tabuleiro)
     pretas=False
   #Caso o jogador queira mover uma dama, primeiro checa-se há cpaturas a serem feitas
   if(escolha=='d' and gameplay_pretas(tabuleiro)=='capturar'):
    while(gameplay(tabuleiro)=='capturar'):
     assinalar_captura_dama(tabuleiro)
     capturar_dama_pretas(tabuleiro)
     posicao(tabuleiro)
     pretas=False
     gameplay_pretas(tabuleiro)
    break
   if(escolha=='d' and gameplay_pretas(tabuleiro)=='mover'):
    mover_dama(tabuleiro)
    posicao(tabuleiro)
    pretas=False
 
 #Atualizando as variáveis de contagem após o movimento das pretas
 n_pecas_brancas=0
 n_pecas_pretas=0
 for i in range(8):
  for j in range(8):
   if(tabuleiro[i][j]=='DB' or tabuleiro[i][j]=='PB'):
    n_pecas_brancas=n_pecas_brancas+1
   if(tabuleiro[i][j]=='DP' or tabuleiro[i][j]=='PP'):
    n_pecas_pretas=n_pecas_pretas+1 
 
 #Atualizando o número de rodadas e as variáveis que permitem o movimento de brancas e negras
 n_rodadas=n_rodadas+1
 print('Rodada {0}'.format(n_rodadas))
 brancas=True
 pretas=True


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#9: Encerramento do jogo

print('Esperamos que tenha se divertido!!!')
print(' ')
print(' ')
print(' ***  ****   ****    *   ***       *      ****    ***     *   *   *')
print('*   * *   *  *   *   *  *   *     * *     *   *  *   *    *   *   *')
print('*   * ****   ****    *  *        *****    *   *  *   *    *   *   *')
print('*   * *   *  *   *   *  * ***   *     *   *   *  *   *             ')
print(' ***  ****   *    *  *   ***   *       *  ****    ***     *   *   *') 
