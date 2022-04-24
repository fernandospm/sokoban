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
# 0 (personaje, espacio)
  if (
      self.mapa[self.personaje_fila][self.personaje_columna] == 0
      and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
  ):   
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.personaje_columna += 1  

# 1 (personaje, meta)
  elif (
        self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
  ):  
        self.mapa[self.personaje_fila][self.personaje_columna] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.personaje_columna += 1 

# 2 (personaje, caja, espacio)
  elif (
         self.mapa[self.personaje_fila][self.personaje_columna] == 0
         and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
         and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
  ):
         self.mapa[self.personaje_fila][self.personaje_columna] = 1
         self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
         self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
         self.personaje_columna += 1 
# 3 (personaje, caja, meta)
  elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 0
          and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
          and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
  ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 1
          self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
          self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
          self.personaje_columna += 1

# 4 (personaje, caja_meta, espacio)
  elif (
        self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
  ):
        self.mapa[self.personaje_fila][self.personaje_columna] = 1
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
        self.personaje_columna += 1 
    
# 5 (personaje, caja_meta, meta)
  elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
  ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1  

# 6 (personaje_meta, espacio)
  elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
  ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1 

# 7 (personaje_meta, meta)
  elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
   ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1  
          
# 8 (personaje_meta, caja, espacio)
  elif (
        self.mapa[self.personaje_fila]  [self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
   ):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
        self.personaje_columna += 1  
          
# 9 (personaje_meta, caja, meta)
  elif (
        self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
  ):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.personaje_columna += 1  

# 10 (personaje_meta, caja_meta, espacio)
  elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
  ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1  
# 11 (personaje_meta, caja_meta_, meta)
  elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 5
          and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
          and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
  ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 4
          self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
          self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
          self.personaje_columna += 1  
  
# 0 (personaje, espacio)
def moverIzquierda(self):
    if (
        self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
  ):
        self.mapa[self.personaje_fila][self.personaje_columna] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.personaje_columna -= 1 
        print("# 0 (personaje, espacio) izquierda")
    
# 1 (personaje, meta)
    elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 0
          and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4
    ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 1
          self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
          self.personaje_columna -= 1
          print("# 1 (personaje, meta) izquierda")

# 2 (personaje, caja, espacio)
    elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 0
          and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
          and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
    ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 1
          self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
          self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
          self.personaje_columna -= 1
          print("# 2 (personaje, caja, espacio) izquierda")

# 3 (personaje, caja, meta)
    elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 0
          and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
          and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
    ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 1
          self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
          self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
          self.personaje_columna -= 1
          print("# 3 (personaje, caja, meta) izquierda")

# 4 (personaje, caja_meta, espacio)
    elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 0
          and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
          and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
    ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 1
          self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
          self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
          self.persoanje_columna -= 1
          print("# 4 (personaje, caja_meta, espacio) izquierda")

# 5 (personaje, caja_meta, meta)
    elif (
          self.mapa[self.personaje_fila][self.personaje_columna] == 0
          and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
          and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
    ):
          self.mapa[self.personaje_fila][self.personaje_columna] = 1
          self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
          self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
          self.personaje_columna -= 1
          print("# 5 (personaje, caja_meta, meta) izquierda")

  
    
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
  
 
  
  
  
  


  
  
  