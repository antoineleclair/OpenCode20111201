<!DOCTYPE html> 
<html> 
<head> 
    <meta charset="utf-8">
    <title>Cody</title> 
    <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
    <script src="/static/js/jquery.min.js"></script>
    ${self.html_head()}
</head>
<body>
    <div class="wrap">
    
        <header>
            <h1>Cody</h1>
            <nav>
                <a href="/">home</a> |
                % if request.user is not None:
                <a href="#">${request.user.name}</a> |
                <a href="${request.route_url('logout')}">logout</a>
                % else:
                <a href="${request.route_url('login')}">login</a> |
                <a href="${request.route_url('user_new')}">register</a>
                % endif
            </nav>
        </header>
        
        <section id="main">
            ${self.body()}
        </section>
        
    </div>
</body>
</html>
<%def name="html_head()"></%def>
