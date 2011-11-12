from cody.tests import TestBase
from pyramid import testing

class HomeTest(TestBase):
    def test_should_return_empty_dict(self):
        from cody.views.home import home
        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual(type(response), dict)
        self.assertEqual(len(response.keys()), 0)
