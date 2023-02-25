from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database creation
engine = create_engine("mysql+mysqlconnector://root:root@192.168.10.18:3307/dbgo")
Session = sessionmaker(bind=engine)
Base = declarative_base()
