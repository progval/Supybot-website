{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<div class="goto_admin">
	Import plugins
	<ul>
		<li><a href="{% url "plugins_submit" %}">Submit your plugins</a></li>
		<li><a href="{% url "plugins_autoimport" %}">Auto-import plugins from Git repo</a></li>
	</ul>
</div>
<h1>
	Your plugins
</h1>
{% if plugins %}
	<table id="plugins">
		<tr>
			<th>Name</th>
			<th>Description</th>
			<th>Published</th>
		</tr>
		{% for plugin in plugins %}
			<tr>
				<td><a href="{% url "plugins_admin_form" plugin.name %}">{{ plugin.name }}</a></td>
				<td>{% autoescape on %}{{ plugin.short_description }}{% endautoescape %}</td>
				<td>{% if plugin.published %}Yes{% else %}No{% endif %}</td>
			</tr>
		{% endfor %}
	</ul>
{% else %}
	<div class="error no-item-on-page">
		Sorry, you didn't submit any plugin for the moment.
	</div>
{% endif %}
{% endblock %}
