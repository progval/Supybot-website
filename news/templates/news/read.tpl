{% extends "base.tpl" %}
{% load heading %}
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
	</table>
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
