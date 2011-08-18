{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<div id="news">
	<dl id="metadata">
		<dt>Author</dt>
		<dd>{{ news.author }}</dd>

		<dt>Created at</dt>
		<dd>{{ news.created_at }}</dd>

		<dt>Last update at</dt>
		<dd>{{ news.updated_at }}</dd>
	</dl>
	<h1>
		{{ news.title }}
	</h1>
	<div id="content">
		{{ news.body|markdown:"safe" }}
	</div>
	<div style="clear: both;"></div>
</div>
{% endblock %}
