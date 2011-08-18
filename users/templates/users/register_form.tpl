{% extends "base.tpl" %}
{% load i18n %}

{% block body %}
{% if error %}
	<div class="error">{{ error }}</div>
{% endif %}
<form action="." method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit" value="Submit" />
</form>
{% endblock %}
