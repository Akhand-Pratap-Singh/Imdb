import json
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from . import schemas, models
from .database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.post('/imdb', status_code = status.HTTP_201_CREATED)
def create(request:schemas.Imdb, db:Session= Depends(get_db)):

	new_value = models.Imdb(popularity=request.popularity,
								director=request.director,
								genre=request.genre,
								imdb_score=request.imdb_score,
								name=request.name)
	db.add(new_value)
	db.commit()
	db.refresh(new_value)
	return new_value

@app.get('/imdb')
def all(name:str, db:Session= Depends(get_db)):
	# import pdb;pdb.set_trace()
	movie = db.query(models.Imdb).filter(models.Imdb.name == name).first()
	try:
	    genre = json.loads(movie.genre)
	except Exception as e:
		genre = movie.genre
	data = {
	        "99popularity":movie.popularity,
	        "director":movie.director,
	        "genre":genre,
	        "imdb_score":movie.imdb_score,
	        "id":movie.id,
	        "name":movie.name
	        }
	if not movie:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f"Movie with the name {name} is not available")

	return data
