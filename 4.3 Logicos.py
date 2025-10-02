'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Operadores Logicos

Los operadores logicos se utilizan con datos bool para hacer evaluaciones mas
complejas donde se requiere que al menos uno sea verdadedo, todos sean
verdaderos, ninguno sea verdadero
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x=4
y=5
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
And

Se utiliza con "and", responde True cuando todas las condiciones se cumplen
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

x==4 and y==5 #Resultado: True ya que ambas condiciones se cumplen
x==4 and y==4 #Resultado: False debido a que una no se cumple
x==5 and y==4 #Resultado: False debido a que una no se cumple


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Or

Se utiliza con "or", responde True cuando al menos una condicion se cumple
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x==4 or y==5 #Resultado: True ya que una condicion se cumplen
x==4 or y==4 #Resultado: True ya que una condicion se cumplen
x==5 or y==4 #Resultado: False debido a que ninguna se cumple

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Not

Se utiliza con "not" responde lo inverso al resultado real, invirtiendolo
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
not(x==4 and y==5) #Resultado: False, ambas se cumplen not invierte a False
not(x==4 or y==4) #Resultado: False, una se cumple, not invierte a False
not(x==5 and y==4) #Resultado: True, ambas no se cumple pero not invierte

