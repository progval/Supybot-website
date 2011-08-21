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
{% if comments %}
	<ul id="comments">
		{% for comment in comments %}
			<li>
				<h2>
				<a name="comm-{{ forloop.counter }}"></a>
				Comment <a href="#comm-{{ forloop.counter }}">#{{ forloop.counter }}</a>
				by {{ comment.user }} at {{ comment.created_date }}
				</h2>
				{% autoescape on %}{{ comment.text|linebreaks }}{% endautoescape %}
			</li>
		{% endfor %}
	</ul>
{% endif %}
{% if user.is_authenticated %}
	<form action="." method="post" id="comment_form" 
		onSubmit="ajaxSendComment(); return false;"> 
		<h2>Leave a comment</h2>
		{% csrf_token %}
		<textarea name="text"></textarea>
		<br />
		<input type="submit" value="Add comment" id="id_submit" />
	</form> 
{% endif %}
{% endblock %}
