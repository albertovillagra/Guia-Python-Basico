'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Operadores de asignacion

Los operadores de asignacion se utilizan para asignar un valor a una variable
pero no solo existe el tradicional "=" si no que hay otros tipos combinados
con aritmeticos, logicos, etc. para acortar codigo. Por ejemplo
x=2
x=x+2
Para no hacer un codigo tan repetitivo, imaginen que no es x si
no variableDeRecoleccion, escribir variableAtrib =variableAtrib+1
ya de por si es extenso. En cambio hacemos:
x+=2 lo que sera lo mismo que escribir x=x+2 o segun el nombre variable
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
+=

Se utiliza para sumar una cantidad, puede ser un numero explicitamente o
una variable. Util para contadores de repeticion
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x+=2 #El valor de x sera 7

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
-=

Todo lo contrario al anterior, resta 1
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x-=2 #El valor de x sera 3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*=

Multiplica por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x*=2 #El valor de x sera 10

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
/=

Divide por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x/=2 #El valor de x sera 2.5


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
%=

Modulo por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x%=2 #El valor de x sera 1

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
//=

Cociente por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x//=2 #El valor de x sera 2

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
**=

Exponente por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x**=2 #El valor de x sera 25

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
&=

And por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x&=2 #El valor de x sera 0

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
|=

Or por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x|=2 #El valor de x sera 7

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
^=

Xor por el valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x^=2 #El valor de x sera 7

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
>>=

Desplazamiento derecha al valor asignado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x>>=2 #El valor de x sera 1

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
<<=

Desplazamiento izquierda al valor dado
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=5
x<<=2 #El valor de x sera 20

