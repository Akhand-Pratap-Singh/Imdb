from pydantic import BaseModel

class Imdb(BaseModel):
	popularity: float
	director: str
	imdb_score: float
	name:str
	genre:str


class User(BaseModel):
	name: str
	email: str
	password: str
	admin_rights: bool