import os
_basedir = os.path.abspath(os.path.dirname(__file__))

#implement session based keying
SECRET_KEY = 'secret_key'

#set debug to false when live
DEBUG = True

#SQLITE DB URI
DB_URI = 'sqlite:///' + os.path.join(_basedir,'models/data/psdata.db')