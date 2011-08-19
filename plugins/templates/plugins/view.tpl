{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<div id="plugin">
	<dl id="metadata">
		<dt>Author</dt>
		<dd>{{ plugin.author }}</dd>

		<dt>Minimal version</dt>
		<dd>{% autoescape on %}{{ plugin.minimal_version }}{% endautoescape %}</dd>

		<dt>Created at</dt>
		<dd>{{ plugin.created_at }}</dd>

		{% if plugin.url %}
			<dt>Website</dt>
			<dd><a href="plugin.url">{{ plugin.url }}</a></dd>
		{% endif %}

		<dt>Git repository</dt>
		<dd>{% autoescape on %}{{ plugin.git_repo }}{% endautoescape %}</dd>
	</dl>
	<h1>{% autoescape on %}{{ plugin.name }}{% endautoescape %}</h1>
	<div id="description">
		{{ plugin.description|markdown:"safe" }}
	</div>
	<div style="clear: both;"></div>
</div>
{% endblock %}
