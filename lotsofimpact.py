# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from database_setup import Regions, Base, ImpactEntry, User


DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL ,convert_unicode=True)

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
User1 = User(name='Niall O\'Hara', email='niall@changex.org',
             picture='https://pbs.twimg.com/profile_images/580423342903148545/C2ZP352K_400x400.png',
             location='Castlebar,Mayo', phone_number='0871131932', job_title='Product Manager', facebook_profile='https://www.facebook.com/nialloh23',
             linkedin_profile='https://www.linkedin.com/in/niallohara1/', twitter_profile='https://twitter.com/nialloh23')

session.add(User1)
session.commit()



User2 = User(name="Paul O'Hara", email="paul@changex.org",
             picture='https://pbs.twimg.com/profile_images/796051821198528512/uR1kI3Xf_400x400.jpg',
             location="Dublin", phone_number="087744782", job_title="CEO ChangeX", facebook_profile="https://www.facebook.com/paul.ohara.33",
             linkedin_profile="https://www.linkedin.com/in/pohara/", twitter_profile="https://twitter.com/pohara")

session.add(User2)
session.commit()



User3 = User(name="Niall O'Hara", email="niall@changex.org",
             picture='https://pbs.twimg.com/profile_images/580423342903148545/C2ZP352K_400x400.png',
             location="Castlebar,Mayo", phone_number="0871131932", job_title="Product Manager", facebook_profile="https://www.facebook.com/nialloh23",
             linkedin_profile="https://www.linkedin.com/in/niallohara1/", twitter_profile="https://twitter.com/nialloh23")

session.add(User1)
session.commit()


User4 = User(name="Niall O'Hara", email="niall@changex.org",
             picture='https://pbs.twimg.com/profile_images/580423342903148545/C2ZP352K_400x400.png',
             location="Castlebar,Mayo", phone_number="0871131932", job_title="Product Manager", facebook_profile="https://www.facebook.com/nialloh23",
             linkedin_profile="https://www.linkedin.com/in/niallohara1/", twitter_profile="https://twitter.com/nialloh23")

session.add(User1)
session.commit()


User5 = User(name="Niall O'Hara", email="niall@changex.org",
             picture='https://pbs.twimg.com/profile_images/580423342903148545/C2ZP352K_400x400.png',
             location="Castlebar,Mayo", phone_number="0871131932", job_title="Product Manager", facebook_profile="https://www.facebook.com/nialloh23",
             linkedin_profile="https://www.linkedin.com/in/niallohara1/", twitter_profile="https://twitter.com/nialloh23")

session.add(User1)
session.commit()








# Region for Mayo
region1 = Regions(user_id=1, name="Mayo", location="Mayo")
session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name='Hosted Local Street Feast', hours='3.5', funding_amount='2300',
                            category='Community', organisation='Street Feast', created_at='03_06_2016',
                            picture='http://streetfeast.ie/wp-content/uploads/2018/05/StreetFeastLibertiesAoifeGiles-1024x922.jpg', address='Castlebar',
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region1, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Volunteered with Local Tidy Towns", hours="2.5", funding_amount='1600',
                            category="Environment", organisation="Castlebar Tidy Towns", created_at="04/07/2016",
                            picture="http://www.millstreet.ie/blog/wp-content/uploads/2012/07/2012_0701July022012cn0017-800.jpg",address="Castlebar",
                            notes="Our team set ourselves a challenge to volunteer with one new community group every month this year. We kicked off this month with the Castlebar Tidy Towns. We helpeed their brilliant team to clean the ringroad around the town!",
                            region=region1, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Helping Start a new Men's Shed", hours="1.0", funding_amount='876',
                            category="Social Isolation", organisation="Men's Shed", created_at="28/05/2016",
                            picture="https://d15afjvg0gyl8n.cloudfront.net/solutions/background_images/000/000/005/hero/mens_shed.jpeg?1488895023",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region1, user_id=1)
session.add(ImpactEntry3)
session.commit()

ImpactEntry4 = ImpactEntry(name="Making Sure Everyone has a Hot Meal this Christmas", hours="7.5", funding_amount='298',
                            category="Homelessness", organisation="Meals on Wheels", created_at="28/12/2016",
                            picture="http://img2.thejournal.ie/article/3761164/river?version=3761219&width=1340",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region1, user_id=1)
session.add(ImpactEntry4)
session.commit()





# Region for Galway
region2 = Regions(user_id=1,name="Galway", location="Galway,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Helping Migrants to Learn English", hours="10.5", funding_amount='5317',
                            category="Inclusion", organisation="Failte Isteach", created_at="18/09/2016",
                            picture="https://d15afjvg0gyl8n.cloudfront.net/solutions/background_images/000/000/008/hero/open-uri20150717-3-1n06qk2?1488895029",address="Booterstown",
                            notes="Our team volunteered at the local community center where we helped recent migrants to Ireland learn english!",
                            region=region2, user_id=2)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Building a new Community Garden", hours="2.0", funding_amount='861',
                            category="Environment", organisation="GIY", created_at="04/07/2016",
                            picture="https://greenvillecommunitygardens.files.wordpress.com/2011/11/gardeningwithkids.jpg",address="Booterstown",
                            notes="Such an amazing day! We helped build a new community garden for Booterstown and will begin growing next year!",
                            region=region2, user_id=2)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Teaching kids to learn to code", hours="1.5", funding_amount='0',
                            category="Education", organisation="Coder Dojo", created_at="25/05/2016",
                            picture="https://d15afjvg0gyl8n.cloudfront.net/solutions/background_images/000/000/004/hero/CoderDojo-Dogpatch.jpg?1488895021",address="Booterstown",
                            notes="Our tech team spent the morning teaching coding skills to an amazing bunch of kids from our local school",
                            region=region2, user_id=2)
session.add(ImpactEntry3)
session.commit()

ImpactEntry4 = ImpactEntry(name="Making Sure Everyone has a Hot Meal this Christmas", hours="7.5", funding_amount='298',
                            category="Homelessness", organisation="Meals on Wheels", created_at="28/12/2016",
                            picture="http://img2.thejournal.ie/article/3761164/river?version=3761219&width=1340",address="Booterstown",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region2, user_id=2)
session.add(ImpactEntry4)
session.commit()






# Region for Sligo
region3 = Regions(user_id=1,name="Sligo", location="Sligo,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Hosted Local Street Feast", hours="3.5", funding_amount='2300',
                            category="Community", organisation="Street Feast", created_at="03/06/2016",
                            picture="http://streetfeast.ie/wp-content/uploads/2018/05/StreetFeastLibertiesAoifeGiles-1024x922.jpg",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region3, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Volunteered with Local Tidy Towns", hours="2.5", funding_amount='1600',
                            category="Environment", organisation="Castlebar Tidy Towns", created_at="04/07/2016",
                            picture="http://www.millstreet.ie/blog/wp-content/uploads/2012/07/2012_0701July022012cn0017-800.jpg",address="Castlebar",
                            notes="Our team set ourselves a challenge to volunteer with one new community group every month this year. We kicked off this month with the Castlebar Tidy Towns. We helpeed their brilliant team to clean the ringroad around the town!",
                            region=region3, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Helping Start a new Men's Shed", hours="1.0", funding_amount='876',
                            category="Social Isolation", organisation="Men's Shed", created_at="28/05/2016",
                            picture="https://d15afjvg0gyl8n.cloudfront.net/solutions/background_images/000/000/005/hero/mens_shed.jpeg?1488895023",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region3, user_id=1)
session.add(ImpactEntry3)
session.commit()

ImpactEntry4 = ImpactEntry(name="Making Sure Everyone has a Hot Meal this Christmas", hours="7.5", funding_amount='298',
                            category="Homelessness", organisation="Meals on Wheels", created_at="28/12/2016",
                            picture="http://img2.thejournal.ie/article/3761164/river?version=3761219&width=1340",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region3, user_id=1)
session.add(ImpactEntry4)
session.commit()








# Region for Leitrim
region4 = Regions(user_id=1,name="Letrim", location="Letrim,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Hosted Local Street Feast", hours="3.5", funding_amount='2300',
                            category="Community", organisation="Street Feast", created_at="03/06/2016",
                            picture="http://streetfeast.ie/wp-content/uploads/2018/05/StreetFeastLibertiesAoifeGiles-1024x922.jpg",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region4, user_id=2)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Volunteered with Local Tidy Towns", hours="2.5", funding_amount='1600',
                            category="Environment", organisation="Castlebar Tidy Towns", created_at="04/07/2016",
                            picture="http://www.millstreet.ie/blog/wp-content/uploads/2012/07/2012_0701July022012cn0017-800.jpg",address="Castlebar",
                            notes="Our team set ourselves a challenge to volunteer with one new community group every month this year. We kicked off this month with the Castlebar Tidy Towns. We helpeed their brilliant team to clean the ringroad around the town!",
                            region=region4, user_id=2)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Helping Start a new Men's Shed", hours="1.0", funding_amount='876',
                            category="Social Isolation", organisation="Men's Shed", created_at="28/05/2016",
                            picture="https://d15afjvg0gyl8n.cloudfront.net/solutions/background_images/000/000/005/hero/mens_shed.jpeg?1488895023",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region4, user_id=2)
session.add(ImpactEntry3)
session.commit()

ImpactEntry4 = ImpactEntry(name="Making Sure Everyone has a Hot Meal this Christmas", hours="7.5", funding_amount='298',
                            category="Homelessness", organisation="Meals on Wheels", created_at="28/12/2016",
                            picture="http://img2.thejournal.ie/article/3761164/river?version=3761219&width=1340",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region4, user_id=2)
session.add(ImpactEntry4)
session.commit()




# Region for Roscommon
region5 = Regions(user_id=1,name="Roscommon", location="Roscommon,Ireland")

session.add(region1)
session.commit()

ImpactEntry1 = ImpactEntry(name="Hosted Local Street Feast", hours="3.5", funding_amount='2,300',
                            category="Community", organisation="Street Feast", created_at="03/06/2016",
                            picture="http://streetfeast.ie/wp-content/uploads/2018/05/StreetFeastLibertiesAoifeGiles-1024x922.jpg",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region5, user_id=1)
session.add(ImpactEntry1)
session.commit()


ImpactEntry2 = ImpactEntry(name="Volunteered with Local Tidy Towns", hours="2.5", funding_amount='1,600',
                            category="Environment", organisation="Castlebar Tidy Towns", created_at="04/07/2016",
                            picture="http://www.millstreet.ie/blog/wp-content/uploads/2012/07/2012_0701July022012cn0017-800.jpg",address="Castlebar",
                            notes="Our team set ourselves a challenge to volunteer with one new community group every month this year. We kicked off this month with the Castlebar Tidy Towns. We helpeed their brilliant team to clean the ringroad around the town!",
                            region=region5, user_id=1)
session.add(ImpactEntry2)
session.commit()

ImpactEntry3 = ImpactEntry(name="Helping Start a new Men's Shed", hours="1.0", funding_amount='870',
                            category="Social Isolation", organisation="Men's Shed", created_at="28/05/2016",
                            picture="https://d15afjvg0gyl8n.cloudfront.net/solutions/background_images/000/000/005/hero/mens_shed.jpeg?1488895023",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region5, user_id=1)
session.add(ImpactEntry3)
session.commit()

ImpactEntry4 = ImpactEntry(name="Making Sure Everyone has a Hot Meal this Christmas", hours="7.5", funding_amount='298',
                            category="Homelessness", organisation="Meals on Wheels", created_at="28/12/2016",
                            picture="http://img2.thejournal.ie/article/3761164/river?version=3761219&width=1340",address="Castlebar",
                            notes="We spent the afternoon helping out an amazing bunch of men who are working to setup a Men's Shed in Castlebar. What an amazing new facility for the people of the town. Delighted to help out",
                            region=region5, user_id=1)
session.add(ImpactEntry4)
session.commit()
