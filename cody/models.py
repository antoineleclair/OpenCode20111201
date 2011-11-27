import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class User(Base):
    """A user of the application, with his credentials."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), unique=True)
    password = Column(Unicode(255))
    name = Column(Unicode(255))
    email = Column(Unicode(255))
    location = Column(Unicode(255))
    
    def __init__(self, username=None, password=None,
                   name=None, email=None, location=None):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.location = location
    
    def __repr__(self):
        return '<User: %s (%s)>' % (self.name, self.username)
        
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
