'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
El segundo tipo de datos de python son las colecciones, esto corresponde a
listas, tuplas, sets y diccionarios.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Listas []
Las listas contienen items de varios tipos primitivos, que no son necesario
de indicar tipo al igual que las variables y son mutable, o sea cambiables.
Se guian por indices y son autoordenadas, sus item se separan por comas.

Las listas se encierran entre corchetes []
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
varLista=[] #lista vacia declarada
varLista1=['a','b','c',1,2,3] #lista con datos tipo int y str

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Tuplas
Las tuplas se comportan igual que las listas, se separan por comas, son auto
ordenadas, se ordenan por indices y contiene varios tipos de datos. La
diferencia radica en que son inmutables por tanto no modificables una vez
creadas.

Las tuplas se encierran entre parentesis ()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
varTupla1=() #Tupla vacia
varTupla2=(False,True,2.4) #Tupla compuesta por bool y float


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Set
Los set se comportan tambien como listas, son mutables, se ordenan por
indices, reciben varios tipos de datos primitivos, pero, son desordenadas
y no aceptan datos duplicados para el mismo tipo

Los set se encierran entre llaves {}
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
varSet1={'1',1} #Almacena '1',1 ya que uno es str y otro int
varSet2={2,2} #almacena solo un 2 ya que esta repetido

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Diccionarios
Los diccionarios se definen por no tener orden y su relacion de datos es
clave : "valor1, valor2", clave2 : "valor1, valor 2" siendo los valores
tipos de datos coleccionables repetibles pero sus claves irrepetibles. Algo
similar a como funciona una tabla con llaves.

Los diccionarios se asignan entre llaves {} y se separa la clave de los
valores con : los valores debe ir entre comillas '' o "" pero las claves
pueden ser tipos primitivos
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
varDiccionario1={
    "Nombres"   : "Esteban, Maria, Claudio",
    "Edades"    : "22, 40, 35",
    1           : {"1,2,3,3"}
}
print (varDiccionario1)
