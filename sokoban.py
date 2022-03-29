class sokoban:
 """
  definir los componentes
  
  0 - personaje
  1 - espacio
  2 - caja
  3 - pared
  4 - meta
  5 - personaje_meta
  6 - caja_meta
  """
 posicion_columna = 4
 mapa = [1,3,3,3,2,3,3,3,1]

 def __init__(self):
  pass #

 def imprimirMapa(self):
     for i in self.mapa:
         if i == 3:
             print(" ", end = "")
         elif i == 2:
            print(chr(64), end = "")
         elif i == 1:
            print("|", end = "")
         else:
           print(i, end = "")
     print()

 def moverDerecha(self):
   self.posicion_columna += 1
   self.mapa[self.posicion_columna] = 2
   self.mapa[self.posicion_columna - 1] = 3
   self.imprimirMapa()
  
 def moverIzquierda(self):
   self.posicion_columna -= 1
   self.mapa[self.posicion_columna] = 2
   self.mapa[self.posicion_columna + 1] = 3
   self.imprimirMapa()
    
juego = sokoban()
juego.imprimirMapa()

instrucciones = "q-Salir\nd-Derecha\na-Izquierda"

while True:
  print(instrucciones)
  movimiento = input("Mover: ")
  if movimiento == "d":
    juego.moverDerecha()
  elif movimiento == "a":
    juego.moverIzquierda()
  elif movimiento == "q":
    print("saliste del juego")
    break
  
  
  
  
  
  


  
  
  