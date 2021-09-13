```py
<!-- admin/user/actions.html -->
{% extends "admin/actions.html" %}
{% block actions-submit %}
    {{ block.super }}
    <button class="button">
        <a href="/tool/update_user_tag/?path={{ request.path }}">一键更新标签</a>
    </button>
{% endblock %}
```