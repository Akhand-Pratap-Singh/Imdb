from sqlalchemy import Column, String, Float
from .database import Base

class Imdb(Base):
	__tablename__ = 'imdb'

	id = Column(Integer, primary_key=True, index = True)
	popularity = Column(Float)
	director = Column(String)
	imdb_score = Column(Float)
	name = Column(String)
	genre = Column(String)
