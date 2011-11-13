<%inherit file="/base.mako"/>

<h1>Users</h1>

<ul>
    % for user in users:
    <li>
        <a href="${request.route_url('user_single', user_id=user.id)}">
            ${user.name} (${user.username})
        </a>
    </li>
    % endfor
</ul>
