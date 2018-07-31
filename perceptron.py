import random

class Perceptron:
  def __init__(self, let_train=0.1):

    #constate de aprendizaje
    self.let_train = let_train

    #arreglo de pesos
    self.w = []

  # Entrena la red
  def train(self, inputs, ouputs):
    # este peso es el bias
    self.w.append(-1);
    # insertamos el numero de pesos dependiendo el numero de entrada
    for i in range(len(inputs[0])):
      self.w.append(0)

    #ponemos la variable de error en 1 para que itere hasta que cumple la condicion
    errors = 1
    while errors != 0:
      #reseteamos el error a cero para saber cuando se marca algun error
      errors = 0
      # recorremos el arreglo de entradas
      for ix in range(len(inputs)):
        #obtenemos la salida del perceptron
        guess = self.guess(inputs[ix])

        #calculamos la actualizacion constanteEntrenamiento*(salidaEsperada - salidaObtenida)
        update = self.let_train*(ouputs[ix] - guess)

        #actualizamos el bias
        self.w[0] += update

        #recorremos todos los pesos
        for i in range(len(self.w)):

          #calculamos la actualizacion del peso
          up = update*inputs[ix][i-1]

          #actualizamos el peso
          self.w[i] += up

          #validamos si el peso da el resultado esperado
          if up != 0: errors +=1

  #Restultado obtenido por el perceptron
  def guess(self, inp):

    #variable inicial para la suma
    suma = 0;

    #recorremos los pesos, debemos tener encuenta que el peso 0 es la bias
    for i in range(1, len(self.w)):
      #sumamos
      suma += inp[i-1] * self.w[i]

    #agregamos el bias  al suma
    suma += self.w[0]

    # Retoramos un valor segun el resultado obtenido (Funcion Escalon)
    return 1 if suma >= 0 else -1

inputs = [
  [-1,-1],
  [-1,1],
  [1,-1],
  [1,1]
]

ouputs = [-1, -1, -1 , 1]

p = Perceptron()
p.train(inputs, ouputs)


x1 = float(input("> "))
x2 = float(input("> "))

print(p.guess([x1,x2]))