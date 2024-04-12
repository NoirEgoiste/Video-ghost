from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/db"
engine = create_engine(DATABASE_URL)
