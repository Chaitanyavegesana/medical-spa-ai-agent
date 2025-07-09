from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace this with your DB URL. Example uses SQLite for simplicity.
DATABASE_URL = "sqlite:///./spa.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Needed only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
