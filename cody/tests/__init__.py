import unittest
from pyramid.config import Configurator
from pyramid import testing
from cody.models import DBSession

def _initTestingDB():
    from sqlalchemy import create_engine
    from cody.models import initialize_sql
    initialize_sql(create_engine('sqlite://'))

class TestBase(unittest.TestCase):
    def setUp(self):
        from cody import add_routes
        self.config = testing.setUp()
        add_routes(self.config)
        _initTestingDB()
        
    def tearDown(self):
        DBSession.remove()
        testing.tearDown()
        
