{% extends "base.tpl" %}
{% load heading %}
{% load markup %}

{% block body %}
<div id="plugin">
	<dl id="metadata">
		<dt>Author</dt>
		<dd>{{ plugin.author }}</dd>

		<dt>Minimal Supybot version</dt>
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

		{% if user = plugin.author %}
			<a href="{% url plugins_admin_form plugin.name %}">Edit this plugin.</a>
			<hr />
		{% endif %}

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
{% if comments %}
	<ul id="comments">
		{% for comment in comments %}
			<li {% ifequal comment.user user %}class="mycomment"{% endifequal %}>
				<dl>
					<dt>
					<a name="comm-{{ forloop.counter }}"></a>
					Comment <a href="#comm-{{ forloop.counter }}">#{{ forloop.counter }}</a>
					by {{ comment.user }} at {{ comment.created_date }}
				</dt>
				<dd>
					{% headingcontext target_level=2 %}{{ comment.text|markdown:"safe" }}{% endheadingcontext %}
				</dd>
			</li>
		{% endfor %}
	</ul>
{% endif %}
{% if user.is_authenticated %}
	<form action="." method="post" id="comment_form">
		<h2>Leave a comment</h2>
		{% csrf_token %}
		<textarea name="text"></textarea>
		<br />
		<input type="submit" value="Add comment" id="id_submit" />
	</form> 
{% endif %}
{% endblock %}
