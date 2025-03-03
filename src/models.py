import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    favoritos=relationship("Favoritos",back_populates="personajes")


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)
    favoritos=relationship("Favoritos",back_populates="planetas")



class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    mail: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    favoritos=relationship("Favoritos",back_populates="usuarios")


class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    user=relationship("Usuarios",back_populates="favoritos")
    personajes_id: Mapped[int] = mapped_column(ForeignKey("personajes.id"))
    personajes=relationship("Personajes",back_populates="favoritos")
    planetas_id: Mapped[int] = mapped_column(ForeignKey("planetas.id"))
    planetas=relationship("Planetas",back_populates="favoritos")
  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
