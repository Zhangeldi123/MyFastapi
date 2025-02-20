from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://zhangeldi:KkhI5zpwaaTZbxWdRxvYYTNQ4nghC4Gm@dpg-curnk2rtq21c73au29eg-a.frankfurt-postgres.render.com/fastapi_7uw0"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функция для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
