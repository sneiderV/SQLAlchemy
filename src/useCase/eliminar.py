from src.modelo.album import Album
from src.modelo.albunCancion import AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.cancion import Cancion
from src.modelo.declarative_base import Session


if __name__ == '__main__':
  
  # Abre la sesion
  session = Session()

  cancion = session.query(Cancion).get(2)
  session.delete(cancion)
  print('La cancion con id 2 fue eliminada')

  session.commit()
  session.close()