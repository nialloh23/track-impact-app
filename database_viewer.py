from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database_setup import Regions, Base, ImpactEntry, User, Friendships
from sqlalchemy import func


engine = create_engine('sqlite:///impactdatabase.db',connect_args={'check_same_thread':False},poolclass=StaticPool)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


total_hours=session.query(func.sum(ImpactEntry.hours)).filter(ImpactEntry.user_id==1)

for result in total_hours.one():
    print result
