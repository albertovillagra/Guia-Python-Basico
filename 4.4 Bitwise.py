'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Operadores Bitwise

Los operadores bitwise se utilizan para manipulacion de datos binarios
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
And

se utiliza con & y este realiza una comparativa a nivel binario (1 y 0) por
cada letra o numero correspondiente a lo que se esta haciendo la operacion
dando 1 si en ambos caso es 1 y 0 en casos contrarios dando como resultado
unna combinacion binaria basada en esto.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=10 #en binario es 1010
b=3  #en binario es 0011
z=x&y
#valor z es 0010 lo que es 2 ya que solo el segundo binario coincide en 1

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Or

Se utiliza con | y este compara tambien binario a binario dando 1 si uno de
los dos es 1 y 0 cuando ambos son 0
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=10 #en binario es 1010
b=3  #en binario es 0011
z=x|y
#valor z es 1011 lo que es 11 ya que 1ro, 2do y 3ro tienen un 1 de uno o ambos

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Xor

Se utiliza con ^ este solo devuevle 1 cuando existe un 1 de un solo lado, pero
no de ambos. En caso contario es 0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=10 #en binario es 1010
b=3  #en binario es 0011
z=x^y
#valor z es 1001 lo que es 9 ya que perimer y ultimo solo tienen 1 de un lado

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Desplazamiento

Se utilizan con >> para desplazar a la derecha o << para la izquierda mas un
numero que indica cuanto se desplazara el binario total hacia uno de los lados.
Cada desplazamiento a la ziquierda genera 0 para rellenar por ejemplo si se
establece a=1 y luego "a << 1" el binario movera el 1 pasando de 1 a 10 y su
valor total de 1 a 2. Cuando se desplaza hacia la derecha va borrando la
cantidad que se mueve por lo que si x=100 y se hace x=x>>2 quedara en 1 pasando
4 a 1.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=10 #en binario es 1010
z=x<< 2 #El valor de z sera 101000 lo que equivale a 16
z=x>>2 #El valor de z sera 10

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Complementario

Se utiliza con ~ este invierte los valores de los decimales pasando 1 a 0
y 0 a 1, pero ademas de esto los transforma a negativo +1 (~x=-(x+1).
Adicional a esto los binarios se definen por octetos para todos los casos,
o sea 8 valores binarios, por lo que usar complementario transformara los 0
a la izquierda sobrante a 1. De todas maneras un binario negativo considera
los 0 como datos y los 1 como sin datos.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=10 #en binario realmente es 00001010
z=x~2 #El valor de z sera -11110101 lo que equivale a -11






