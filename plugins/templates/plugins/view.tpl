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

		<hr />

		<dt>Score</dt>
		<dd>{{ score }}</dd>

		<dt>Number of votes</dt>
		<dd>{{ num_votes }}</dd>

		<dt>Your vote</dt>
		<dd>
			{% if user.is_authenticated %}
				<form action="." method="POST">
					{% csrf_token %}
					<input type="submit" name="-1" value="-1" {% if myvote.is_downvote %}disabled="disabled"{% endif %} />
					
					<input type="submit" name="0" value=" 0 " {% if not myvote.is_downvote and not myvote.is_upvote %}disabled="disabled"{% endif %} />
					
					<input type="submit" name="+1" value="+1" {% if myvote.is_upvote %}disabled="disabled"{% endif %} />
				</form>
			{% else %}
				You must be <a href="{% url users_login %}">logged in</a> to vote.
			{% endif %}
		</dd>
	</dl>
	<h1>{% autoescape on %}{{ plugin.name }}{% endautoescape %}</h1>
	<div id="description">
		{{ plugin.description|markdown:"safe" }}
	</div>
	<div style="clear: both;"></div>
</div>
{% endblock %}
