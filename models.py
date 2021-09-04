from sqlalchemy import Column, String, Integer, Float
from database import Base

class Imdb(Base):
	__tablename__ = 'imdb'

	id = Column(Integer, primary_key=True, index = True)
	popularity = Column(Float)
	director = Column(String)
	imdb_score = Column(Float)
	name = Column(String)
	genre = Column(String)

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index = True)
	name = Column(String)
	email = Column(String)
	password = Column(String)
	admin_rights = Column(Boolean, default=False)

class User(BaseModel):
	name: str
	email: str
	password: str
	admin_rights: bool