from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Regions, Base, ImpactEntry, User

engine = create_engine('sqlite:///impactdatabase.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Niall O'Hara", email="niall@changex.org",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png', location="Castlebar,Mayo")
session.add(User1)
session.commit()

User2 = User(name="Paul O'Hara", email="paul@changex.org",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png', location="Castlebar,Mayo")
session.add(User2)
session.commit()






# Region for Mayo
region1 = Regions(user_id=1, name="Mayo", location="Mayo")
session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region1, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region1, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region1, user_id=1)
session.add(ImpactEntry3)
session.commit()







# Region for Galway
region2 = Regions(user_id=1,name="Galway", location="Galway,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region2, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region2, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region2, user_id=1)
session.add(ImpactEntry3)
session.commit()






# Region for Sligo
region3 = Regions(user_id=1,name="Sligo", location="Sligo,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region3, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region3, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region3, user_id=1)
session.add(ImpactEntry3)
session.commit()








# Region for Leitrim
region4 = Regions(user_id=1,name="Letrim", location="Letrim,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region4, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region4, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region4, user_id=1)
session.add(ImpactEntry3)
session.commit()




# Region for Roscommon
region5 = Regions(user_id=1,name="Roscommon", location="Roscommon,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region5, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region5, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Built Mens Shed", hours="4",
                     funding_amount="1100", category="Mental Health", notes="Fantastic to meet new people",picture="image", address="Castlebar",region=region5, user_id=1)
session.add(ImpactEntry3)
session.commit()
