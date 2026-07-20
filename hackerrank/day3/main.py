if __name__ == '__main__':
    N = int(input('Diguite un numero entero: ').strip())

'''
tarea: Dado un numero entero n, realiza las siguientes acciones condicionales:
1 Si N es impar, imprime Weird.
2 Si N es par y esta en el rango inclusivo de 2 a 5, imprime Not Weird.
3 Si N es par y esta en el rango inclusivo de 6 a 20, imprime Weird.
4 Si N es par y es mayor que 20, imprime Not Weird.
'''


if(N%2  !=  0):
    print('Weird')
elif (N%2  == 0 and N >= 2 and N <= 5):
    print('Not Weird')
elif (N%2 == 0 and N >= 6 and N <= 20):
        print('Weird')
elif (N%2 == 0 and N > 20):
    print('Not Weird')
       