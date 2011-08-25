{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<h1>
	Import plugins from repository {{ repository.name }}
</h1>
<form action="." method="post">
	{% csrf_token %}
	<table id="plugins">
		<tr>
			<th>Name</th>
			<th>Import?</th>
			<th>Already in the database?</th>
			<th>By you?</th>
		</tr>
		{% for plugin in plugins %}
			<tr>
				{% if plugin.in_database %}
					<td>{{ plugin.name }}</td>
					<td><input type="checkbox" name="import_plugin_{{ plugin.name }}" disabled="disabled" /></td>
					<td>Yes</td>
					<td>{% if plugin.in_database.author = user %}Yes{% else %}No{% endif %}</td>
				{% else %}
					<td>{{ plugin.name }}</td>
					<td><input type="checkbox" name="import_plugin_{{ plugin.name }}" /></td>
					<td colspan="2">No</td>
				{% endif %}
			</tr>
		{% endfor %}
		<tr>
			<td colspan="4">
				<input type="submit" value="Submit" class="submit" />
			</td>
		</tr>
	</table>
</form>
{% endblock %}
