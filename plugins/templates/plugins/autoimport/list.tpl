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
			<th>Already in the database?</th>
			<th>By you?</th>
			<th>Import?</th>
		</tr>
		{% for plugin in plugins %}
			<tr>
				<td>{{ plugin.name }}</td>
				{% if plugin.in_database %}
					<td>Yes</td>
					<td>{% if plugin.in_database.user = user %}Yes{% else %}No{% endif %}</td>
					<td><input type="checkbox" name="import_plugin_{{ plugin.name }}" disabled="disabled" /></td>
				{% else %}
					<td colspan="2">No</td>
					<td><input type="checkbox" name="import_plugin_{{ plugin.name }}" /></td>
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