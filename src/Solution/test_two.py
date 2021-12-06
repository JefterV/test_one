"""
Escreva uma função que recebe como argumentos duas matrizes de inteiros.
Sua função precisa determinar se o segundo array é uma subsequência do primeiro, retornando verdadeiro ou falso;
"""

def is_subsequence(array_one, array_two) -> bool:
    index = 0
    response = True

    for key in range(1,len(array_one), 2):
        if not array_one[key] == array_two[index]: 
            response = False 
            break
        index += 1
                     
    return response
    
            


if __name__=="__main__":
        array_one = [5, 1, 22, 25, 6, -1, 8, 10]
        array_two = [1, 6, -1, 10]

        print(is_subsequence(array_one, array_two))