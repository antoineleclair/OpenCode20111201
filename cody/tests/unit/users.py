from cody.tests  import TestBase
from pyramid import testing

class TestNew(TestBase):
    def test_returns_new_empty_user(self):
        from cody.views.users import new
        from cody.models import User
        request = testing.DummyRequest()
        response = new(request)
        self.assertEqual(type(response), dict)
        self.assertTrue('user' in response)
        user = response['user']
        self.assertEqual(type(user), User)
        self.assertIsNone(user.username)
        self.assertIsNone(user.password)
        self.assertIsNone(user.name)
        self.assertIsNone(user.location)

class TestCreate(TestBase):
    def test_redirects_to_user_profile_when_valid(self):
        from cody.views.users import create
        from cody.models import User
        from pyramid.httpexceptions import HTTPFound
        request = testing.DummyRequest()
        request.params['username'] = u'john55'
        request.params['password'] = u'password'
        request.params['name'] = u'John Doe'
        request.params['email'] = u'user@example.com'
        request.params['location'] = u'Quebec'
        response = create(request)
        self.assertEqual(type(response), HTTPFound)
        self.assertEqual(response.location, 'http://example.com/users/1')
        
    def test_creates_user_when_valid(self):
        from cody.views.users import create
        from cody.models import User
        from pyramid.httpexceptions import HTTPFound
        from cody.models import DBSession
        request = testing.DummyRequest()
        request.params['username'] = u'john55'
        request.params['password'] = u'password'
        request.params['name'] = u'John Doe'
        request.params['email'] = u'user@example.com'
        request.params['location'] = u'Quebec'
        response = create(request)
        session = DBSession()
        user = DBSession.query(User).one()
        self.assertEqual(user.username, u'john55')
        self.assertGreater(len(user.password), 0)
        self.assertEqual(user.name, u'John Doe')
        self.assertEqual(user.email, u'user@example.com')
        self.assertEqual(user.location, u'Quebec')

class TestIndex(TestBase):
    def test_returns_list_of_all_users(self):
        from cody.views.users import index
        from cody.models import DBSession, User
        session = DBSession()
        session.add(User())
        session.add(User())
        session.add(User())
        request = testing.DummyRequest()
        response = index(request)
        self.assertEqual(type(response), dict)
        self.assertTrue('users' in response)
        self.assertEqual(response['users'].count(), 3)
