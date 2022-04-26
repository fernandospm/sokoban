from os import system, name
from time import sleep
class Sokoban:
 """_summary_: Sokoban class"""
    
"""
      Description: Sokoban game template
      0 - Character
      1 - Floor
      2 - Box
      3 - Wall
      4 - Target
      5 - Box_Target
      6 - Character_Target
  """
map = []
"""nivel =open("Nivel.1","r")"""

character_row = 3
character_col = 3

def loadMap(self,lvl):
        if lvl == 1:
          self.nivel=open("Nivel.1", "r")
        else:
          self.nivel=open("Nivel.2", "r")
        self.map = []
        for  row in self.nivel:
            linea = []
            for digito in row:
                if digito == "\n":
                    continue
                linea.append(int(digito))
            self.mapa.append(linea)
    

def printMap(self):
        """_summary_: Print the map"""
        # TODO: Print the map
        for row in self.map:  # For each row in map
            print(row)  # Print the row

def findCharacterPosition(self):
        """_summary_: Find the character position"""
        for row in range(len(self.map)):  # Get rows number on the map
            for col in range(len(self.map[row])):  # Get columns number on the map
                if self.map[row][col] == 3:  # If the character is found
                    self.character_row = row  # Update the character row position
                    self.character_col = col  # Update the character col position

def moveLeft(self):
        """_summary_: Move the character to the left rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col - 1] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][self.character_col] = 1  # put floor character last position
            self.map[self.character_row][self.character_col - 1] = 0  # move the character to next position
            self.character_col = self.character_col - 1  # update the character position
        # TODO: 1. character, target
        elif (
          self.map[self.character_row][self.character_col] == 0
          and self.map[self.character_row][self.character_col - 1] == 4
        ):
          self.map[self.character_row][self.character_col_] = 1
          self.map[self.personaje_fila][self.personaje_columna - 1] = 5
          self.character_col = self.character_col - 1
          print("# 1 (personaje, meta) izquierda")
        # TODO: 2. character, box, floor
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row][self.character_col - 1] == 2
              and self.map[self.character_row][self.character_col - 2] == 1
        ):
              self.map[self.character_row][self.character_col] = 1
              self.map[self.character_row][self.character_col - 1] = 0
              self.map[self.character_row][self.character_col - 2] = 2
              self.character_col = self.character_col - 1
              print("# 2 (personaje, caja, espacio) izquierda")
        # TODO: 3. character, box, target
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row][self.character_col - 1] == 2
              and self.map[self.character_row][self.character_col - 2] == 4
        ):
              self.map[self.character_row][self.character_col] = 1
              self.map[self.character_row][self.character_col - 1] = 0
              self.map[self.character_row][self.character_col - 2] = 6
              self.character_col = self.character_col - 1
              print("# 3 (personaje, caja, meta) izquierda")
        # TODO: 4. character, box_target, floor
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row][self.character_col - 1] == 6
              and self.map[self.character_row][self.character_col - 2] == 1
        ):
              self.map[self.character_row][self.character_col] = 1
              self.map[self.character_row][self.character_col - 1] = 5
              self.map[self.character_row][self.character_col - 2] = 2
              self.character_col = self.character_col - 1
              print("# 4 (personaje, caja_meta, espacio) izquierda")

          # TODO: 5. character, box_target, target
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row][self.character_col - 1] == 6
              and self.map[self.character_row][self.character_col - 2] == 4
        ):
              self.map[self.character_row][self.character_col] = 1
              self.map[self.character_row][self.character_col - 1] = 5
              self.map[self.character_row][self.character_col - 2] = 6
              self.character_col = self.character_col - 1
              print("# 5 (personaje, caja_meta, meta) izquierda")

         # TODO: 6. character_taget, floor
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row][self.character_col - 1] == 1
             
        ):
              self.map[self.character_row][self.character_col] = 4
              self.map[self.character_row][self.character_col - 1] = 0
              self.character_col = self.character_col - 1
              print("# 6 (personaje_meta, espacio) izquierda")

        # TODO: 7. character_taget, target
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row][self.character_col - 1] == 4
             
        ):
              self.map[self.character_row][self.character_col] = 4
              self.map[self.character_row][self.character_col - 1] = 5
              self.character_col = self.character_col - 1
              print("# 6 (personaje_meta, meta) izquierda")
        # TODO: 8. character_taget, box, floor
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row][self.character_col - 1] == 2
              and self.map[self.character_row][self.character_col - 2] == 1
        ):
              self.map[self.character_row][self.character_col] = 4
              self.map[self.character_row][self.character_col - 1] = 0
              self.map[self.character_row][self.character_col - 2] = 2
              self.character_col = self.character_col - 1
              print("# 6 (personaje_meta, caja, espacio) izquierda")
        # TODO: 9. character_taget, box, target
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row][self.character_col - 1] == 2
              and self.map[self.character_row][self.character_col - 2] == 4
        ):
              self.map[self.character_row][self.character_col] = 4
              self.map[self.character_row][self.character_col - 1] = 0
              self.map[self.character_row][self.character_col - 2] = 6
              self.character_col = self.character_col - 1
              print("# 6 (personaje_meta, caja, meta) izquierda")
        # TODO: 10. character_taget, box_target, floor
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row][self.character_col - 1] == 6
              and self.map[self.character_row][self.character_col - 2] == 1
        ):
              self.map[self.character_row][self.character_col] = 4
              self.map[self.character_row][self.character_col - 1] = 5
              self.map[self.character_row][self.character_col - 2] = 2
              self.character_col = self.character_col - 1
              print("# 6 (personaje_meta, caja_meta, espacio) izquierda")
        # TODO: 11. character_taget, box_target, target
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row][self.character_col - 1] == 2
              and self.map[self.character_row][self.character_col - 2] == 4
        ):
              self.map[self.character_row][self.character_col] = 4
              self.map[self.character_row][self.character_col - 1] = 5
              self.map[self.character_row][self.character_col - 2] = 6
              self.character_col = self.character_col - 1
              print("# 6 (personaje_meta, caja_meta, meta) izquierda")

def moveRight(self):
        """_summary_: Move the character to the right rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][self.character_col] = 1  # put floor character last position
            self.map[self.character_row][self.character_col + 1] = 0  # move the character to next position
            self.character_col = self.character_col + 1  # update the character position
        # TODO: 1. character, target
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 4
        ):  
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row][self.character_col + 1] = 5  
            self.character_col = self.character_col + 1
        # TODO: 2. character, box, floor
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 2
            and self.map[self.character_row][self.character_col + 2] == 1
        ):  
            self.map[self.character_row][self.character_col] = 1 
            self.map[self.character_row][self.character_col + 1] = 0 
            self.map[self.character_row][self.character_col + 2] = 2
            self.character_col = self.character_col + 1
        # TODO: 3. character, box, target
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 4
            and self.map[self.character_row][self.character_col + 2] == 2
        ):  
            self.map[self.character_row][self.character_col] = 1 
            self.map[self.character_row][self.character_col + 1] = 0 
            self.map[self.character_row][self.character_col + 2] = 6
            self.character_col = self.character_col + 1
        # TODO: 4. character, box_target, floor
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 6
            and self.map[self.character_row][self.character_col + 2] == 1
        ):  
            self.map[self.character_row][self.character_col] = 1 
            self.map[self.character_row][self.character_col + 1] = 5
            self.map[self.character_row][self.character_col + 2] = 2
            self.character_col = self.character_col + 1
        # TODO: 5. character, box_target, target
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row][self.character_col + 1] == 6
            and self.map[self.character_row][self.character_col + 2] == 4
        ):  
            self.map[self.character_row][self.character_col] = 1 
            self.map[self.character_row][self.character_col + 1] = 5 
            self.map[self.character_row][self.character_col + 2] = 6
            self.character_col = self.character_col + 1
        # TODO: 6. character_taget, floor
        elif (
            self.map[self.character_row][self.character_col] == 1
            and self.map[self.character_row][self.character_col + 1] == 5
        ):  
            self.map[self.character_row][self.character_col] = 0
            self.map[self.character_row][self.character_col + 1] = 4
            self.character_col = self.character_col + 1
        # TODO: 7. character_taget, target
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row][self.character_col + 1] == 4
        ):  
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row][self.character_col + 1] = 5 
            self.character_col = self.character_col + 1
        # TODO: 8. character_taget, box, floor
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row][self.character_col + 1] == 2
            and self.map[self.character_row][self.character_col + 2] == 1
        ):  
            self.map[self.character_row][self.character_col] = 4
            self.map[self.character_row][self.character_col + 1] = 0 
            self.map[self.character_row][self.character_col + 2] = 2
            self.character_col = self.character_col + 1
        # TODO: 9. character_taget, box, target
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row][self.character_col + 1] == 2
            and self.map[self.character_row][self.character_col + 2] == 4
        ):  
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row][self.character_col + 1] = 0 
            self.map[self.character_row][self.character_col + 2] = 6
            self.character_col = self.character_col + 1
        # TODO: 10. character_taget, box_target, floor
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row][self.character_col + 1] == 6
            and self.map[self.character_row][self.character_col + 2] == 1
        ):  
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row][self.character_col + 1] = 5 
            self.map[self.character_row][self.character_col + 2] = 2
            self.character_col = self.character_col + 1
        # TODO: 11. character_taget, box_target, target
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row][self.character_col + 1] == 6
            and self.map[self.character_row][self.character_col + 2] == 4
        ):  
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row][self.character_col + 1] = 5
            self.map[self.character_row][self.character_col + 2] = 6
            self.character_col = self.character_col + 1

def moveUp(self):
        """_summary_: Move the character up rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row - 1][self.character_col] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][self.character_col] = 1  # put floor character last position
            self.map[self.character_row - 1][self.character_col] = 0  # move the character to next position
            self.character_row = self.character_row - 1  # update the character position
        # TODO: 1. character, target
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row - 1][self.character_col] == 4
        ):  
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row - 1][self.character_col] = 5
            self.character_row = self.character_row - 1 
        # TODO: 2. character, box, floor
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row - 1][self.character_col] == 2
              and self.map[self.character_row - 2][self.character_col] == 1
        ):  
              self.map[self.character_row][self.character_col] = 1  
              self.map[self.character_row - 1][self.character_col] = 0
              self.map[self.character_row - 2][self.character_col] = 2
              self.character_row = self.character_row - 1 
        # TODO: 3. character, box, target
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row - 1][self.character_col] == 2
              and self.map[self.character_row - 2][self.character_col] == 1
        ):  
              self.map[self.character_row][self.character_col] = 1  
              self.map[self.character_row - 1][self.character_col] = 0
              self.map[self.character_row - 2][self.character_col] = 2
              self.character_row = self.character_row - 1
        # TODO: 4. character, box_target, floor
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row - 1][self.character_col] == 6
              and self.map[self.character_row - 2][self.character_col] == 1
        ):  
              self.map[self.character_row][self.character_col] = 1  
              self.map[self.character_row - 1][self.character_col] = 5
              self.map[self.character_row - 2][self.character_col] = 2
              self.character_row = self.character_row - 1
        # TODO: 5. character, box_target, target
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row - 1][self.character_col] == 6
              and self.map[self.character_row - 2][self.character_col] == 4
        ):  
              self.map[self.character_row][self.character_col] = 1  
              self.map[self.character_row - 1][self.character_col] = 5
              self.map[self.character_row - 2][self.character_col] = 6
              self.character_row = self.character_row - 1
        # TODO: 6. character_taget, floor
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row - 1][self.character_col] == 1
        ):  
              self.map[self.character_row][self.character_col] = 4  
              self.map[self.character_row - 1][self.character_col] = 0
              self.character_row = self.character_row - 1
        # TODO: 7. character_taget, target
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row - 1][self.character_col] == 4     
        ):  
              self.map[self.character_row][self.character_col] = 4  
              self.map[self.character_row - 1][self.character_col] = 5
              self.character_row = self.character_row - 1
        # TODO: 8. character_taget, box, floor
        elif (
              self.map[self.character_row][self.character_col] == 0
              and self.map[self.character_row - 1][self.character_col] == 2
              and self.map[self.character_row - 2][self.character_col] == 1
        ):  
              self.map[self.character_row][self.character_col] = 4 
              self.map[self.character_row - 1][self.character_col] = 0
              self.map[self.character_row - 2][self.character_col] = 2
              self.character_row = self.character_row - 1
        # TODO: 9. character_taget, box, target
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row - 1][self.character_col] == 2
              and self.map[self.character_row - 2][self.character_col] == 4
        ):  
              self.map[self.character_row][self.character_col] = 4  
              self.map[self.character_row - 1][self.character_col] = 0
              self.map[self.character_row - 2][self.character_col] = 6
              self.character_row = self.character_row - 1
        # TODO: 10. character_taget, box_target, floor
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row - 1][self.character_col] == 6
              and self.map[self.character_row - 2][self.character_col] == 1
        ):  
              self.map[self.character_row][self.character_col] = 4 
              self.map[self.character_row - 1][self.character_col] = 5
              self.map[self.character_row - 2][self.character_col] = 2
              self.character_row = self.character_row - 1
        # TODO: 11. character_taget, box_target, target
        elif (
              self.map[self.character_row][self.character_col] == 5
              and self.map[self.character_row - 1][self.character_col] == 6
              and self.map[self.character_row - 2][self.character_col] == 4
        ):  
              self.map[self.character_row][self.character_col] = 4  
              self.map[self.character_row - 1][self.character_col] = 5
              self.map[self.character_row - 2][self.character_col] = 6
              self.character_row = self.character_row - 1

def moveDown(self):
        """_summary_: Move the character down rules"""
        # 0. character, floor
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 1
        ):  # If the character is on the floor and the next position is a floor
            self.map[self.character_row][self.character_col] = 1  # put floor character last position
            self.map[self.character_row + 1][self.character_col] = 0  # move the character to next position
            self.character_row = self.character_row + 1  # update the character position
        # TODO: 1. character, target
        if (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 4
        ):  
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row + 1][self.character_col] = 5  
            self.character_row = self.character_row + 1 
        # TODO: 2. character, box, floor
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 2
            and self.map[self.character_row + 2][self.character_col] == 1
        ): 
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row + 1][self.character_col] = 0 
            self.map[self.character_row + 2][self.character_col] = 2
            self.character_row = self.character_row + 1 
        # TODO: 3. character, box, target
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 1
            and self.map[self.character_row + 2][self.character_col] == 4
        ): 
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row + 1][self.character_col] = 0 
            self.map[self.character_row + 2][self.character_col] = 6
            self.character_row = self.character_row + 1 
        # TODO: 4. character, box_target, floor
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 6
            and self.map[self.character_row + 2][self.character_col] == 1
        ): 
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row + 1][self.character_col] = 5
            self.map[self.character_row + 2][self.character_col] = 2 
            self.character_row = self.character_row + 1 
        # TODO: 5. character, box_target, target
        elif (
            self.map[self.character_row][self.character_col] == 0
            and self.map[self.character_row + 1][self.character_col] == 6
            and self.map[self.character_row + 2][self.character_col] == 4
        ): 
            self.map[self.character_row][self.character_col] = 1  
            self.map[self.character_row + 1][self.character_col] = 5 
            self.map[self.character_row + 2][self.character_col] = 6 
            self.character_row = self.character_row + 1 
        # TODO: 6. character_taget, floor
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row + 1][self.character_col] == 1  
        ): 
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row + 1][self.character_col] = 0 
            self.character_row = self.character_row + 1 
        # TODO: 7. character_taget, target
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row + 1][self.character_col] == 4
        ): 
            self.map[self.character_row][self.character_col] = 4
            self.map[self.character_row + 1][self.character_col] = 5 
            self.character_row = self.character_row + 1 
        # TODO: 8. character_taget, box, floor
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row + 1][self.character_col] == 2
            and self.map[self.character_row + 2][self.character_col] == 1
        ): 
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row + 1][self.character_col] = 0 
            self.map[self.character_row + 2][self.character_col] = 2 
            self.character_row = self.character_row + 1 
        # TODO: 9. character_taget, box, target
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row + 1][self.character_col] == 2
            and self.map[self.character_row + 2][self.character_col] == 4
        ): 
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row + 1][self.character_col] = 0 
            self.map[self.character_row + 2][self.character_col] = 6 
            self.character_row = self.character_row + 1 
        # TODO: 10. character_taget, box_target, floor
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row + 1][self.character_col] == 6
            and self.map[self.character_row + 2][self.character_col] == 1
        ): 
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row + 1][self.character_col] = 5 
            self.map[self.character_row + 2][self.character_col] = 2 
            self.character_row = self.character_row + 1 
        # TODO: 11. character_taget, box_target, target
        elif (
            self.map[self.character_row][self.character_col] == 5
            and self.map[self.character_row + 1][self.character_col] == 6
            and self.map[self.character_row + 2][self.character_col] == 4
        ): 
            self.map[self.character_row][self.character_col] = 4 
            self.map[self.character_row + 1][self.character_col] = 5 
            self.map[self.character_row + 2][self.character_col] = 6 
            self.character_row = self.character_row + 1 

def play(self):
    instrucciones="a-izquierda\nd-derecha\nw-arriba\ns-abajo"
    print(instrucciones)
    lvl = 1
    while True:
      self.leerMapa(lvl)
      print(f"\nNivel {lvl}")
      self.imprimirMapa()
      while True:
        movimiento = input("Mover Hacia: ")
        if movimiento == "d":
          self.moverDerecha()
        elif movimiento == "a":
          self.moverIzquierda()
        elif movimiento == "w":
          self.moverArriba()
        elif movimiento == "s":
          self.moverAbajo()
        elif movimiento == "q":
          print("salir del juego")
          break
        else: 
          pass
          self.borrarS()
          print(f"\nNivel {lvl}")
          fin = self.imprimirMapa()
          if fin:
           print("Has completado el nivel!!!")
           print("SIGUIENTE NIVEL")
          lvl = 2
          # espera 3 segundos para cambiar de nivel
          "sleep(3)"
          self.borrarS()
          break
game = Sokoban()  
game.Play()
