from .database import Base, engine, SessionLocal
from . import models, schemas, crud, routes

# Create the database tables
models.Base.metadata.create_all(bind=engine)