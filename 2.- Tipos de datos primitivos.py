'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
A pesar que las variables se puede asignar sin la obligacion de indicarles
su tipo de datos, es posible hacerlo si requerimos que sea un tipo obligatorio
como un numero que sea tipo str en vez de int. Estos tipos de datos son tipos
primitivos y los veremos asignandolos a variables
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Int / Integer

Numeros enteros de tipo int que es abreviacion de integer
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var1=int(10) #se asigna 10 como int, no es necesario ya que con solo indicar
             #10 es

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Float / Floating

Numeros decimales son tipo float abreviacion de floating
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var2=float(3)#Se asignara 3 a un float lo que lo dejara como 3.0

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Str / String

Palabras  son tipo str que es abreviacion de string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var3=str(10) #se asigna 10 como str a pesar que no se encierra en '' 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Bool / Boolean

True o False respetando su primera en mayusculas son tipo bool, abreviacion
    de booleano que es utilizado para indicar si algo es verdadero o falso
    a veces se usan numeros como 1 y 0
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var4=bool(1) #bool tambien acepta 1 y 0, 1 True 0 False
var5=True #Aisgnado como True, debe ir sin comillas y la T en mayusculas
var6=False #Aisgnado como False, debe ir sin comillasla y la F en mayusculas

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Python no acepta, como js con let, que una variable sea declarada sin datos
lo que provoca un error
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#var7=

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Otros Tipos Primitivos no tan usados
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Bytes
Dato primitivo que se indica con b'' sea para texto, numero, etc. pero debe
ir entre comillas. Es utizado para que luego mediante un print del texto
indexado de su valor ascii. No funciona con el valor completo solo indices
y es inmutable o sea  ose puede cambiar

Indiexacion lo veremos mas adelante
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var8=b"Hola" #La variable tiene asignado b"Hola" realmente

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Byte Array

Funciona del a misma forma que byte pero este si es mutable
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var9=vytearray(b'Hola')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
None

Es un tipo de datos unico y que indica que su valor es nulo o none
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var10=None

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Existen otros como complex, range, memoryview y frozenset que no se abordaran
pero puedes investigarlos
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
