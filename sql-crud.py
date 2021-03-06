from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from our localhost chinook db

db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the programmer table
class Programmer(base):
    __tablename__= "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)


# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# create records on our Programmer table

# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer",
# )


alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing",
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

johan_coetzee = Programmer(
    first_name="Johan",
    last_name="Coetzee",
    gender="M",
    nationality="South African",
    famous_for="Being Me"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(johan_coetzee)

# commit our session to the database
# session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World President"

# commit our session to the database
# session.commit()

# update multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male" 
#     else:
#         print("Gender not defined") 
#     session.commit()    

programmer = session.query(Programmer).filter_by(id=2).first()
session.delete(programmer)
session.commit()


# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "

    )

