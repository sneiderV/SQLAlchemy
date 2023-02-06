from src.modelo.albunCancion import AlbumCancion
from src.modelo.album import Album
from src.modelo.cancion import Cancion
from src.modelo.declarative_base import Session
from src.modelo.interprete import Interprete

if __name__ == '__main__':
  
  # Abre la sesion
  session = Session()
  
  cancion = session.query(Cancion).get(2)
  print('Se editara la cancion con id 2')
  interprete = session.query(Interprete).get(4)

  cancion.minutos = 5
  cancion.segundos = 30
  cancion.compositor = "Pedro Pérez"
  cancion.interpretes.append(interprete)
  
  session.add(cancion)

  session.commit()
  print('Cancion editada')
  session.close()