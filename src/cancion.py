from sqlalchemy import Column, Integer, String
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Cancion(Base) :
    __tablename__ = 'cancion'

    # Attributes
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)

    # Relations
    interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')
    albumes = relationship('Album',secondary='album_cancion')
    
