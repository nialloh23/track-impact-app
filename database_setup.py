import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
import os
#

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    location = Column(String(250))
    picture = Column(String(250))
    phone_number = Column(String(80))
    job_title = Column(String(80))
    facebook_profile = Column(String(80))
    twitter_profile = Column(String(80))
    linkedin_profile = Column(String(80))
    bio = Column(String(250))
    familyName = Column(String(80))
    timezone= Column(String(80))
    geo_city= Column(String(80))
    geo_state= Column(String(80))
    geo_country= Column(String(80))
    geo_lat= Column(Float)
    geo_lng= Column(Float)
    website= Column(String(80))
    avatar= Column(String(250))
    employment_name= Column(String(80))
    employment_title= Column(String(80))
    employment_role= Column(String(80))
    employment_domain= Column(String(80))
    employment_seniority= Column(String(80))
    facebook_handle= Column(String(80))
    github_handle= Column(String(80))
    github_avatar= Column(String(250))
    twitter_id= Column(String(80))
    twitter_followers= Column(Integer)
    twitter_following= Column(Integer)
    twitter_avatar= Column(String(250))

class Regions(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'location' : self.location,
            'user_id' : self.user_id
            }

class ImpactEntry(Base):
    __tablename__ = 'impact_entry'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    hours = Column(Float)
    funding_amount = Column(Numeric(15,2))
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
    latitude = Column(Float)
    longitude = Column(Float)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'hours' : self.hours,
            'funding_amount' : self.funding_amount,
            'category' : self.category,
            'organisation' : self.organisation,
            'created_at' : self.created_at,
            'notes' : self.notes,
            'picture' : self.picture,
            'address' : self.address,
            'region_id' : self.region_id,
            'user_id' : self.user_id
            }

class Friendships(Base):
    __tablename__ = 'friendships'

    id = Column(Integer, primary_key=True)
    follower = Column(Integer,ForeignKey('user.id'))
    followed = Column(Integer)
    user = relationship(User)



DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL ,convert_unicode=True)

Base.metadata.create_all(engine)
