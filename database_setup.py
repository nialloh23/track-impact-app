import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    location = Column(String(250))
    picture = Column(String(80))
    phone_number = Column(String(80))
    job_title = Column(String(80))
    facebook_profile = Column(String(80))
    twitter_profile = Column(String(80))
    linkedin_profile = Column(String(80))

class Regions(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class ImpactEntry(Base):
    __tablename__ = 'impact_entry'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    hours = Column(String(8))
    funding_amount = Column(String(8))
    category = Column(String(80))
    organisation = Column(String(80))
    created_at = Column(String(80))
    notes = Column(String(250))
    picture = Column(String(250))
    address= Column(String(80))
    region_id = Column(Integer, ForeignKey('regions.id'))
    region = relationship(Regions)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


engine = create_engine('sqlite:///impactdatabase.db')


Base.metadata.create_all(engine)
