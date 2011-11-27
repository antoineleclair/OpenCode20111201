from datetime import timedelta
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from cody.models import DBSession, User
from cody.lib.mailer import send_welcome_email

@view_config(route_name='users',
    request_method='GET', renderer='/users/index.mako')
def index(request):
    """List all the users."""
    session = DBSession()
    users = session.query(User).order_by(User.username)
    return {'users': users}

@view_config(route_name='user_new',
    request_method='GET', renderer='/users/new.mako')
def new(request):
    """Form to register."""
    return {'user': User()}
    
@view_config(route_name='users',
    request_method='POST', renderer='/users/new.mako')
def create(request):
    """Receives data to register a user."""
    # TODO workshop: validation
    # TODO workshop: encrypt password
    username = request.params['username']
    password = request.params['password']
    name = request.params['name']
    email = request.params['email']
    location = request.params['location']
    user = User(username, password, name, email, location)
    session = DBSession()
    session.add(user)
    session.flush()
    # TODO workshop: test email by mocking
    send_welcome_email(request.registry.settings, name, email)
    response = HTTPFound(route_url('user_single', request, user_id=user.id))
    # totally insecure, TODO in workshop: use auth token or something
    response.set_cookie('user_id', str(user.id), max_age=timedelta(30))
    return response
    
@view_config(route_name='user_single',
    request_method='GET', renderer='/users/show.mako')
def show(request):
    """Shows the profile of a user."""
     # TODO workshop: write a test
     # TODO workshop: not found
    session = DBSession()
    user = session.query(User).get(request.matchdict['user_id'])
    return {'user': user}
    
# TODO workshop: a user can edit his profile
