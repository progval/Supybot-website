{% extends "base.tpl" %}

{% block body %}
{% if plugin %}
	<h1>Edit plugin {{ plugin.name }}</h1>
{% else %}
	<h1>New plugin submission</h1>
{% endif %}
{% if saved %}
	<div class="saved">
		Your plugin has been successfully submitted.
		You can now edit it.
	</div>
{% endif %}
<form action="." method="POST">
	{% csrf_token %}
	<table class="form">{{ form.as_table }}
	<tr><td colspan="2"><input type="submit" value="Submit" /></td></tr>
	</table>
</form>
{% endblock %}

