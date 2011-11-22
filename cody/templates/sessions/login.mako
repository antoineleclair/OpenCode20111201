<%inherit file="/base.mako"/>

<h1>Login</h1>

<form action="" method="post">
    <div>
        <label for="username">Username</label>
        <input type="text" name="username"  id="username" value="${username}"/>
    </div>
    <div>
        <label for="password">Password</label>
        <input type="password" name="password"  id="password"/>
    </div>
    <div>
        <input type="submit" value="Let me in"/>
    </div>
</form>
