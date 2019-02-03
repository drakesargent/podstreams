import dbconn as db
import datetime as date

user1 = db.User(name="Admin")
db.addItem(item=user1)

categories = []

categories.append(db.Category(name="podcast", user=user1))
categories.append(db.Category(name="VOD", user=user1))
categories.append(db.Category(name="live stream", user=user1))
categories.append(db.Category(name="blog", user=user1))
categories.append(db.Category(name="vlog", user=user1))

for cat in categories:
    db.addItem(cat)
    print("added{}".format(cat.name))

shows = []

eqpsf = db.Show(title="ExQueerience Points: Starfinder",
                link="https://www.exqueeriencepoints.com",
                user=user1)

shows.append(eqpsf)

eqpq = db.Show(title="ExQueerience Points: Qmenera",
               link="https://www.exqueeriencepoints.com",
               user=user1)

shows.append(eqpq)

for show in shows:
    db.addItem(show)
    print("added {}".format(show.title))

scl1 = db.ShowCatLink(user=user1, show=eqpsf, category=categories[0])
scl2 = db.ShowCatLink(user=user1, show=eqpq, category=categories[0])

db.addItem(scl1)
db.addItem(scl2)

comText1 = '''A delightful space/sci-fi tabletop RPG real-play podcast featuring
              lgbtq+ voices. They play a game produced by Paizo called
              Starfinder. The story they follow is a completely homebrewed
              adventure cooked up from the mind of their talented Game 
              Master.'''
comText2 = '''Another real-play tabletop RPG podcast featuring all lgbtq+
              voices. The game is Numenera produced by MonteCook Games. Taking
              place in the Nineth World setting and utilizing the mechanics of
              the Cypher System, Qmenera takes it's players into a mysterious
              world where technology and magic are intertwined.'''

comm1 = db.Comment(user=user1, show=eqpsf, text=comText1,
                   createDate=date.datetime.now())
comm2 = db.Comment(user=user1, show=eqpq, text=comText2,
                   createDate=date.datetime.now())

db.addItem(comm1)
db.addItem(comm2)
