from pyramid.view import view_config
from cody.models import DBSession, User

@view_config(route_name='users',
    request_method='GET', renderer='/users/index.mako')
def index(request):
    """List all the users."""
    session = DBSession()
    users = session.Query(User).order_by(User.username)
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
    # TODO register user and redirect, show form if invalid
    return {'user': user}

@view_config(route_name='user_single',
    request_method='GET', renderer='/users/show.mako')
def show(request):
    """Shows the profile of a user."""
    session = DBSession()
    user = session.Query(User).get(request.matchdict['user_id'])
    # TODO if not found
    return {'user': user}
