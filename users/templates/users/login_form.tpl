{% extends "base.tpl" %}

{% block body %}
{% if error %}
	<div class="error">{{ error }}</div>
{% endif %}
<form action="." method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit" value="Submit" />
</form>
<a href="../register/?next={{ next }}">Click here</a> if you do not have an account yet, in order
to create an account.
{% endblock %}
