from modelo.cancion import Cancion
from modelo.declarative_base import Session


if __name__ == '__main__':
  
  # Abre la sesion
  session = Session()

  cancion = session.query(Cancion).get(2)
  session.delete(cancion)
  print('La cancion fue eliminada')

  session.commit()
  session.close()