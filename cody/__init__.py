from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from cody.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'cody:static', cache_max_age=3600)
    add_routes(config)
    config.scan('cody')
    return config.make_wsgi_app()

def add_routes(config):
    """Adds the routes to the application."""
    config.add_route('home', '/')
    config.add_route('users', '/users')
    config.add_route('user_edit', '/users/{user_id}/edit')
    config.add_route('user_new', '/users/new')
    config.add_route('user_single', '/users/{user_id}')
