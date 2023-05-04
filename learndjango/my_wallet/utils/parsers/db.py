from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

def get_connection_dsn() -> str:
    return (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DBNAME')}"
    )


metadata = MetaData()
Base = declarative_base()
Base.metadata = metadata

db = create_engine(get_connection_dsn(), echo=False)
metadata.reflect(bind=db)

news = metadata.tables['my_wallet_news']

sm = sessionmaker(bind=db, autoflush=True, expire_on_commit=True)
session = scoped_session(sm)

class News(Base):
    __tablename__ = "my_wallet_news"
