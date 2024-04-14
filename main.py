import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Real, Roleta, Heurístico, Creep, 1% por geracao, x²+y²+(3x+4y-26)², x E [0, 10], y E [0, 20]
pop_usuario = int(input("Deseja definir alguma população inicial, caso não digite valores menores ou iguais a 0: "))
pop_computador = 10000
populacao = 0
num_geracoes = int(input("Qual a quantidade de gerações que deseja testar: "))
orderedFitness = []
anterior = int()
melhores_individuos = []
cont_cruz=0
orderedNewFitness=[]
cont_ger=0

if(pop_usuario > 0):
    populacao = pop_usuario
else:
    populacao = pop_computador

def fitness(curPopulation, currX, currY):
    if(curPopulation != 0 and (currX >= 0 and currX <= 10) and (currY >= 0 and currY <= 20)):
        fit = pow(currX, 2) + pow(currY, 2) + pow(((3 * currX) + (4 * currY) - 26), 2)
        orderedFitness.append({"x": currX, "y": currY, "fitness": fit})
        curPopulation -= 1
        currX= random.uniform(0.0 , 10.0)
        currY= random.uniform(0.0 , 20.0)
        fitness(curPopulation, currX, currY)


def selecao():
    totalFitness = sum(item["fitness"] for item in orderedFitness)
    numeroSorteio = random.uniform(0, totalFitness) # Sorteia um número entre 0 e o fitness para servir de base para a seleção de indivíduos
    somadorFitness = 0
    for item in orderedFitness:
        somadorFitness += item["fitness"]
        if somadorFitness > numeroSorteio:
            return item

def cruzamento():
    for cont_cruz in range (populacao): 
        dad1 = selecao()
        dad2 = selecao()
        x_dad1 = dad1["x"]
        y_dad1 = dad1["y"]
        fit_dad1 = dad1["fitness"]

        x_dad2 = dad2["x"]
        y_dad2 = dad2["y"]
        fit_dad2 = dad2["fitness"]
        r = random.uniform(0, 1)
        if (fit_dad1 >= fit_dad2):
            x_filho = x_dad1 + r*(x_dad2 - x_dad1)
            y_filho = y_dad1 + r*(y_dad2 - y_dad1)
        else: 
            x_filho = x_dad2 + r*(x_dad1 - x_dad2)
            y_filho = y_dad2 + r*(y_dad1 - y_dad2)
        fit_filho = pow(x_filho, 2) + pow(y_filho , 2) + pow(((3 * x_filho) + (4 * y_filho) - 26), 2)
        orderedNewFitness.append({"x": x_filho, "y": y_filho, "fitness": fit_filho})
    elitismo()
    return

def mutacaoCreepUniforme(individuo, sigma=0.1):
    valor = random.gauss(0, sigma) # Gera um valor entre 0 e sigma
    individuo["x"] += valor
    individuo["y"] += valor
    return individuo

def mutacaoCreepNaoUniforme(individuo, Liminf, Limsup, i):
    z = random.randint(0, 1) # Gera um valor binário para decidir se vai somar ou subtrair
    delta = random.random() # Gera um valor para ser multiplicado
    if z == 1:
        individuo["x"] += delta * (i, Limsup - individuo["x"])
        individuo["y"] += delta * (i, Limsup - individuo["y"])
    else:
        individuo["x"] -= delta * (i, individuo["x"] - Liminf)
        individuo["y"] -= delta * (i, individuo["y"] - Liminf)
    return individuo

def elitismo():
    pop_001 = int(0.01 * populacao)
    orderedFitness.sort(key=lambda x: x["fitness"] , reverse=True)  
    print(melhores_individuos)         
    melhores_individuos = orderedFitness[:pop_001]               #pegando o 1% mais promissor da geração dos pais
    del orderedNewFitness[:pop_001]                          #deletando os piores individuos da nova geração
    
    orderedNewFitness.extend(melhores_individuos)            #juntando os melhores individuos da antiga geração com a nova geração
    orderedFitness.clear()                      
    orderedFitness.extend(orderedNewFitness)        
    orderedNewFitness.clear()

def plotagem():
    x_values = [item["x"] for item in orderedFitness]
    y_values = [item["y"] for item in orderedFitness]
    fitness_values = [item["fitness"] for item in orderedFitness]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_values, y_values, fitness_values, c='r', marker='o')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fitness')
    plt.show()

fitness(populacao, 0, 0)
print("Escolha o tipo de mutacao \n-[1] Creep Uniforme \n-[2] Creep Não Uniforme")
mutacaoOp = int(input())
for cont_ger in range(num_geracoes):
    cruzamento()
    selecionado = selecao() # Seleciona o indivíduo, será feito o cruzamento e a mutação
    if mutacaoOp == 1:
        selecionadoMutacao = mutacaoCreepUniforme(selecionado)
    elif mutacaoOp == 2:
        selecionadoMutacao = mutacaoCreepNaoUniforme(selecionado, 0, 10, 20) # Limite inferior, limite superior, i = 20
    else: 
        print("Opção inválida")

    if orderedFitness:
        # Encontra o dicionário com o maior valor de fitness
        melhor_individuo = max(orderedFitness, key=lambda x: x["fitness"])

        print("Melhor indivíduo:")
        print("x:", melhor_individuo["x"])
        print("y:", melhor_individuo["y"])
        print("fitness:", melhor_individuo["fitness"])

        plotagem()
    else:
        print("Nenhum dado fitness foi calculado.")



