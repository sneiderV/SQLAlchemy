from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base

class Interprete(Base):
    __tablename__ = 'interprete'

    # Attributes
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    # Relations
    cancion = Column(Integer, ForeignKey('cancion.id'))