from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base

class AlbumCancion(Base):
    __tablename__ = 'album_cancion'

    # Attribute
    
    # Relations
    album_id = Column(
        Integer, 
        ForeignKey('album.id'), 
        primary_key=True)
    
    cancion_id = Column(
        Integer, 
        ForeignKey('cancion.id'), 
        primary_key=True)

