#############################################################################################################################################################################################################################
#Nome do projeto: Project Estatistica Aplicada
#Description  : Apresentar tabela de Calculo de Variância conforme instruções
#Author        : Gabriela Terixeira / Renato Rocha
#Email        : gabyteixeiragt2@gmail.com
#Created        : 28/04/2022
##########################################################################################################################################################################################################################"""

'''
Instruções
Desenvolver um programa em Python com as seguintes características.
Ler uma arquivo TXT com dados numéricos
Calcular e apresentar as seguintes medidas:
Máximo
Mínimo
Amplitude
Média
Mediana
Variância 
Desvio Padrão
Não utilizem bibliotecas
Individual ou em duplos
Anexar o arquivo Py (ou qualquer outra linguagem)
'''

#__________________________Lista: doc ____________________________
import os
caminho_dados = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dados.txt")

print(caminho_dados)

nome_tabela= input("\nQual o nome da tabela?\n")
#nome_tabela= "Minha Tabela de Variância"
with open (caminho_dados,"r") as arquivo: #Abrir arquivo txt
    doc= arquivo.read().split("\n") #ler arquivo txt e armazenar dados em uma lista de string que chamamos de "doc"

#__________________________Lista convertida: doc_int ____________________________

doc_int=list(map(int,doc)) # transformar lista de strings em uma lista de numeros inteiros (que chamamos de doc_int)

#__________________________Calculos da Tabela ____________________________

#------------Calculando valor maximo------------

f_Max = max(doc_int) #Função max() retorna o maior valor na lista


#------------Calculando valor minimo------------

f_Min = min(doc_int) ##Função min() retorna o menor valor na lista

#------------Calculando valor minimo------------

amp = f_Max - f_Min #Retorna a Amplitude

#------------Calculando a média------------

media = sum(doc_int)/len(doc_int) #álculo da média 
# Funçãoção sum() soma todos os elementos da lista 
# Função len() retorna a quantidade de elementos da lista


#------------Calculando a mediana------------

med=doc_int #Criando uma variavel "med" para conter os dados da lista "doc_int"
n=len(med) #Configurando a variável "n" para representar a quantidade de elementos da lista "med"
med.sort() #Coloca os elementos da lista "med" em ordem crescente

#identificando se a quantidade de elementos da lista "med" é par ou impar
#Divisão "//" arredonda o resultado de uma divisão de decimal para inteiro (se um valor der "5.4" ela retorna "5")

if n % 2 == 0: #se "n" for par
    mediana = (med[n//2] + med[n//2 - 1])/2
    #Utilizamos o n//2 para gerar o indice de lista onde localizaremos o primeiro valor para calcular a mediana
    #Utilizamos o n//2-1 para gerar o indice de lista onde localizaremos o segundo valor para calcular a mediana
    
else: #se "n" for impar
    mediana = med[n//2] #Utilizamos o n//2 para gerar o indice de lista onde localizaremos o primeiro valor para calcular a mediana

#------------Calculando a Variância------------

desvios = list(num - media for num in doc_int)
'''
Calculo de desvios:
Leia-se: Para cada "item" na lista "doc_int", subtraia "itemx" pela média. 
Quando terminar, armazene o resultado de cada subtração em uma lista
'''

desvios_ao2 = list(num * num for num in desvios)
'''
Calculo de desvios elevados ao quadrado:
Leia-se: Para cada "item" na lista "desvios", multiplique "itemx" * "itemx". 
Quando terminar, armazene o resultado de cada multiplicação em uma lista
'''
while True:
    tipo_var = int(input("\nQual o tipo de dados? \n \n[1] Populacao \n[2] Amostra \n \nDigite 1 ou 2 para selecionar o tipo de dados: "))
    if tipo_var == 1:
        var = sum(desvios_ao2)/len(desvios_ao2) #Calculo da variância populacional
        break
    elif tipo_var == 2:
        var = sum(desvios_ao2)/(len(desvios_ao2)-1) #Calculo da variância amostral
        break
    else:
        print ("\nDigite 1 ou 2 para selecionar o tipo de dados!\n")



#------------Calculando o Desvio Padrao------------

desvpad=var**0.5 #Calculo do desvio padrão, ou seja, raiz quadrada da variante

#------------Calculando o Coeficiente de Variação------------

CV = (desvpad/media) #Calculo do Coeficiente de Variação, ou seja, Desvio Padrão dividido pela média

#__________________________Design da Tabela ____________________________


print("\nComo deseja visualizar a tabela? \n \n[1] Visualização Padrao \n[2] Visualização mais Bonitinha \n")

while True:
  #mvt=Modo de Visualizacao da Tabela
  mvt=int(input("Selecione um modo de visualização: "))
  if mvt == 1:
    #\n = quebra de linha
    print("\n")
    #{:>X}.format= ">" direcao do espaçamento da formatação "X" quantidade de espaçamento da formatação.
    print ('{:>30}'.format(nome_tabela))
    print ('{:<25} {:<25.2f}'.format('Máximo', f_Max))
    print ('{:<25} {:<25.2f}'.format('Mínimo', f_Min))
    print ('{:<25} {:<25.2f}'.format('Amplitude', amp))
    print ('{:<25} {:<25.2f}'.format('Média', media))
    print ('{:<25} {:<25.2f}'.format('Mediana', mediana))
    print ('{:<25} {:<25.2f}'.format('Variância', var))
    print ('{:<25} {:<25.2f}'.format('Desvio Padrão', desvpad))
    print ('{:<25} {:<25.2%}'.format('C.V.', CV))
    #pra converter um decimal em porcentagem como ".format" basta colocar { : .n%
    break
  elif mvt == 2:
    print("\n")
    print ("_"*39)
    print("  ")
    print (nome_tabela.center(39))
    print ("_"*39)
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:>1}'.format("|", "Máximo", "|", f_Max, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:>1}'.format("|", "Mínimo", "|", f_Min, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:>1}'.format("|", "Amplitude", "|", amp, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:>1}'.format("|", "Média", "|", media, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:<0}'.format("|", "Mediana", "|", mediana, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:<0}'.format("|", "Variância", "|", var, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2f}' '{:<0}'.format("|", "Desvio Padrão", "|", desvpad, " |"))
    print ('{:<1} {:<15} {:<10} {:<8.2%}' '{:<0}'.format("|", "C.V.", "|", CV, " |"))
    print ("|_____________________________________|")
    break
  else:
    print ("\nDigite 1 ou 2 para apresentação do modo!\n")


arquivo.close