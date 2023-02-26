from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

time.sleep(2)
# Database creation
engine = create_engine("mysql+mysqlconnector://api_user:api_pass@192.168.10.18:3307/dbapi")
Session = sessionmaker(bind=engine)
Base = declarative_base()
