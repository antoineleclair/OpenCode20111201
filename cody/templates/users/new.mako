<%inherit file="/base.mako"/>

<h1>Register</h1>

<form action="${request.route_url('users')}" method="post">
    <div>
        <label for="username">Username</label>
        <input type="text" name="username" id="username" value="${user.username}"/>
    </div>
    <div>
        <label for="password">Password</label>
        <input type="password" name="password" id="password"/>
    </div>
    <div>
        <label for="name">Name</label>
        <input type="text" name="name" id="name" value="${user.name}"/>
    </div>
    <div>
        <label for="email">Email</label>
        <input type="text" name="email" id="email" value="${user.email}"/>
    </div>
    <div>
        <label for="location">Location</label>
        <input type="text" name="location" id="location" value="${user.location}"/>
    </div>
    <div>
        <input type="submit" value="Register"/>
    </div>
</form>
