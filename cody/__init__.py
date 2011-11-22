from pyramid.config import Configurator
from pyramid.events import NewRequest
from sqlalchemy import engine_from_config
from cody.models import initialize_sql, DBSession, User

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'cody:static', cache_max_age=3600)
    add_routes(config)
    config.scan('cody')
    config.add_subscriber(add_user_to_request, NewRequest)        
    return config.make_wsgi_app()

def add_user_to_request(event):
    """Event subscriber to add the user to the request if any.
    If user not logged in, request.user is None.
    """
    # totally insecure TODO workshop: use auth token or something
    try:
        user_id = int(event.request.cookies['user_id'])
    except (ValueError, KeyError):
        event.request.user = None
        return
    session = DBSession()
    event.request.user = session.query(User).get(user_id)


def add_routes(config):
    """Adds the routes to the application."""
    config.add_route('home', '/')
    
    config.add_route('users', '/users')
    config.add_route('user_edit', '/users/{user_id}/edit')
    config.add_route('user_new', '/users/new')
    config.add_route('user_single', '/users/{user_id}')
    
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
