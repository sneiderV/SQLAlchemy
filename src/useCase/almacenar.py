# from src.modelo.cancion import Cancion
from modelo.cancion import Cancion
from modelo.interprete import Interprete
from modelo.album import Album, Medio
from modelo.declarative_base import Base, engine, Session

if __name__ == '__main__':
    
    #Crear la BD
    Base.metadata.create_all(engine)

    # Abre la sesion
    session = Session()

    #Crear interpretes
    i1 = Interprete(nombre = "Samuel Torres", texto_curiosidades = "Es colombiano y vive en NY")
    i2 = Interprete(nombre = "Aldo Gavilan", texto_curiosidades = "Cantó a Cuba")
    i3 = Interprete(nombre = "Buena Vista Social club")
    i4 = Interprete(nombre = "Arturo Sandoval", texto_curiosidades = "No sabía quien era")
    session.add(i1)
    session.add(i2)
    session.add(i3)
    session.add(i4)
    session.commit()
    print('Se agregan los interpretes')

    # Crear álbumes
    a1 = Album(titulo = "Latin Jazz Compilation", ano = 2021, descripcion = "Album original", medio = Medio.DISCO)
    a2 = Album(titulo = "Bandas sonoras famosas", ano = 2021, descripcion = "Compilación", medio = Medio.DISCO)
    session.add(a1)
    session.add(a2)

    # Crear canciones
    c1 = Cancion(titulo = "Ajiaco", minutos = 3, segundos = 1, compositor = "Samuel Torres")
    c2 = Cancion(titulo = "Forced Displacement", minutos = 3, segundos = 12, compositor = "Desconocido")
    c3 = Cancion(titulo = "Alegría", minutos = 4, segundos = 27, compositor = "AU")
    session.add(c1)
    session.add(c2)
    session.add(c3)

    # Relacionar albumes con canciones
    a1.canciones = [c1, c2]
    a2.canciones = [c1, c3]

    # Relacionar canciones con intérpretes
    c1.interpretes = [i1]
    c2.interpretes = [i2]
    c3.interpretes = [i3, i4]

    print('Se agregan los datos y sus relaciones')
    session.commit()
    session.close()

   