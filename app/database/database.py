from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

time.sleep(2)
# Database creation
engine = create_engine("mysql+mysqlconnector://api_user:api_pass@database:3306/dbapi")
Session = sessionmaker(bind=engine)
Base = declarative_base()
