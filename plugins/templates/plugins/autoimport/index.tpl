{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<h1>
	Your Git repositories
</h1>
<form action="." method="post">
	{% csrf_token %}
	<table id="new_repo">
		<tr><th colspan="2">Register a new repository</th></tr>
		{{ form.as_table }}
		<tr><td colspan="2"><input type="submit" value="Submit" class="submit" /></td></tr>
	</table>
</form>
{% if repositories %}
	<table id="repositories">
		<tr>
			<th>Name</th>
			<th>URL</th>
			<th>State</th>
			<th>Latest pull</th>
			<th>Actions</th>
		</tr>
		{% for repo in repositories %}
			<tr>
				<td>{{ repo.name }}</td>
				<td>{{ repo.url }}</td>
				<td>
					{% ifequal repo.state "c" %}cloning{% endifequal %}
					{% ifequal repo.state "o" %}ok{% endifequal %}
					{% ifequal repo.state "w" %}working{% endifequal %}
					{% ifequal repo.state "n" %}failed{% endifequal %}
				</td>
				<td>
					{% if repo.state = "o" %}
						{{ repo.latest_fetch }}
					{% else %}
						none / unknown
					{% endif %}
				<td>
					<a href="{% url "plugins_autoimport_repo" repo.name %}">import</a>
					<a href="{% url "plugins_autoimport_delrepo" repo.name %}">delete</a>
				</td>
			</tr>
		{% endfor %}
	</table>
{% else %}
	<div class="error no-item-on-page">
		You didn't register any git repository for the moment.
	</div>
{% endif %}
{% endblock %}
