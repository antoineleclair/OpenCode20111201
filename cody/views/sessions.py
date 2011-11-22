from datetime import timedelta
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from cody.models import User, DBSession

@view_config(route_name='login',request_method='GET',
    renderer='/sessions/login.mako')
def login_form(request):
    return {'username': None}

@view_config(route_name='login',request_method='POST',
    renderer='/sessions/login.mako')
def login(request):
    username = request.params.get('username', None)
    password = request.params.get('password', None)
    session = DBSession()
    user = session.query(User).filter(User.username==username).first()
    if user is not None and user.password == password:
        response = HTTPFound('/')
         # totally insecure, TODO in workshop: use auth token or something
        response.set_cookie('user_id', str(user.id), max_age=timedelta(30))
        return response
    return {'username': username}

@view_config(route_name='logout',request_method='GET')
def logout(request):
    response = HTTPFound('/')
    response.delete_cookie('user_id')
    return response
