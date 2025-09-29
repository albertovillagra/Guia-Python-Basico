'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
A pesar que las variables se puede asignar sin la obligacion de indicarles
su tipo de datos, es posible hacerlo si requerimos que sea un tipo obligatorio
como un numero que sea tipo str en vez de int. Estos tipos de datos son tipos
primitivos y los veremos asignandolos a variables
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Numeros enteros son tipos int que es abreviacion de integer
Numeros decimales son tipo float
Palabras  son tipo str que es abreviacion de string, si no se formatean con
    un tipo definido previo o durante la asignacion debe ir entre comillas
    simples o dobles '' o ""
True o False respetando su primera en mayusculas son tipo bool, abreviacion
    de booleano que es utilizado para indicar si algo es verdadero o falso
    a veces se usan numeros como 1 y 0
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Indicando el tipo primitivo a variables
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var1=int(10) #se asigna 10 como int, no es necesario ya que con solo indicar
             #10 es suficiente
var2=str(10) #se asigna 10 como str a pesar que no se encierra en '' o ""
var3=bool(1) #bool tambien acepta 1 y 0, 1 True 0 False
var4=float(3)#Se asignara 3 a un float lo que lo dejara como 3.0
var5='' #tipo str pero vacio


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Python no aceta, como js con let, que una variable sea declarada sin datos
lo que provoca un error
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
var6=
