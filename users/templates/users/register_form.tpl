{% extends "base.tpl" %}
{% load i18n %}

{% block body %}
{% if error %}
	<div class="error">{{ error }}</div>
{% endif %}
<form action="." method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<div class="honey">
		<label of="honey">Don't edit this field.</label>
		<input type="text" name="honey" value="pot" />
	</div>
	<input type="submit" value="Submit" />
</form>
{% endblock %}
