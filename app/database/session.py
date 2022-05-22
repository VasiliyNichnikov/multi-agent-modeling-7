from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.utils.paths import get_db_url

DATABASE_URL = get_db_url()

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
