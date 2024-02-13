import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('host')
database = os.getenv('database')
user = os.getenv('user')
password = os.getenv('password')



url = URL.create(
    database=database,
    username=user,
    password= password,
    host=host,
    drivername="postgresql"
)


engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()
Base.prepare(autoload_with=engine)

combined_Database_Class = Base.classes.student_course
Students_Database_Class = Base.classes.students
Courses_Database_Class = Base.classes.courses
Academies_Database_Class = Base.classes.academies

