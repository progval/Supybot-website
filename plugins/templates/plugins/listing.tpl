{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<div class="goto_admin">
	<a href="{% url plugins_admin_index %}">Administrate your plugins</a><br />
	<a href="{% url plugins_submit %}">Submit your plugins</a>
</div>
<h1>
	Latest plugins
</h1>
{% if page.has_other_pages %}
	<div id="pagination">
		{% if page.has_previous %}
		<a href="{% url news_listing page.previous_page_number %}">&lt;=</a>
		{% endif %}
		<strong>{{ page.number }}</strong>
		{% if page.has_next %}
			<a href="{% url news_listing page.next_page_number %}">=&gt;</a>
		{% endif %}
	<div>
{% endif %}
{% if page.object_list %}
	<table id="plugins">
		<tr>
			<th>Name</th>
			<th>Author</th>
			<th>Description</th>
			<th>Links</th>
		</tr>
		{% for plugin in page.object_list %}
			<tr>
				<td><a href="{% url plugins_view plugin.name %}">{{ plugin.name }}</a></td>
				<td>{{ plugin.author }}</td>
				<td>{% autoescape on %}{{ plugin.short_description }}{% endautoescape %}</td>
				<td>
					{% if plugin.url %}<a href="{{ plugin.url }}">doc</a>{% endif %}
					{% if plugin.git_repo %}<a href="{% autoescape on %}{{ plugin.git_repo }}{% endautoescape %} ">git</a>{% endif %}
				</td>
			</tr>
		{% endfor %}
	</ul>
{% else %}
	<div class="error no-item-on-page">
		Sorry, no plugins published at the moment.
	</div>
{% endif %}
{% endblock %}
