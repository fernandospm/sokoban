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

mapa = [
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
 [1,3,3,1,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1],
 [1,3,3,1,3,2,3,3,3,3,3,3,0,3,3,1,1,1,1,1],
 [1,3,0,1,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,1],
 [1,3,3,0,3,3,3,0,3,3,3,3,3,3,3,3,4,4,4,1],
 [1,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,4,4,4,1],
 [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,1],
 [1,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1],
 [1,3,3,0,3,3,3,3,3,3,0,3,3,3,3,1,1,1,1,1],
 [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1],
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
 ]

muneco_fila = 2
muneco_columna = 5

def imprimirMapa(self):
  for fila in self.mapa:
   print(fila)
    
def jugar(self):
 self.imprimirMapa()

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
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
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


  
  


  
  
  