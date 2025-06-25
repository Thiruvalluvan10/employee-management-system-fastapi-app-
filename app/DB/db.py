from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:Thiruvalluvan%4010@localhost:3306/EMS"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def init_db():
    SQLModel.metadata.create_all(engine)
