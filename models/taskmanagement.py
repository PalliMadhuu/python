from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine=create_engine('postgressql+psycopg2://postgres:Mm2%404%406%408%400@localhost:5432/taskmanagement')

Base=declarative_base()


    