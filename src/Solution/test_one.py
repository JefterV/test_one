""" 
Escreva uma função que recebe como argumentos: uma matriz de inteiros distintos e um inteiro (valor de destino).
Você precisa verificar se quaisquer dois números da matriz somam o valor alvo.
Se for esse o caso, sua função deve retornar esses dois números em forma de array. Caso contrário, apenas retorne um array vazio.
"""


def two_sum(array, target) -> list:
        ResponseArray = []
        soma = int
        
        for key, value in enumerate(array):
            for key02, value02 in enumerate(array):
                if key == key02: continue

                soma = value + value02

                if soma == target:
                    ResponseArray.append(value)
                    ResponseArray.append(value02)
                    return ResponseArray
                    
        return ResponseArray
        
            






if __name__=="__main__":
        array_one = [3, 5, -4, 8, 11, 1, -1, 6]
        target = 10

        print(two_sum(array_one,target))