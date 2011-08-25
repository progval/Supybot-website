{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<div class="goto_admin">
	For plugin developpers:
	<ul>
		<li><a href="{% url plugins_admin_index %}">Administrate your plugins</a></li>
		<li><a href="{% url plugins_submit %}">Submit your plugins</a></li>
		<li><a href="{% url plugins_autoimport %}">Auto-import plugins from Git repo</a></li>
	</ul>
</div>
<h1>
	Latest plugins
</h1>
<ul id="feeds">
	<li><a type="application/rss+xml" href="/plugins/feeds/rss/updates">RSS feed</a></li>
	<li><a type="application/atom+xml" href="/plugins/feeds/atom/updates">Atom feed</a></li>
</ul>
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
{% if plugins %}
	<table id="plugins">
		<tr>
			<th>Name</th>
			<th>Author</th>
			<th>Description</th>
			<th>Ratings</th>
			<th>Links</th>
		</tr>
		{% for plugin in plugins %}
			<tr>
				<td><a href="{% url plugins_view plugin.name %}">{{ plugin.name }}</a></td>
				<td>{{ plugin.author }}</td>
				<td>{% autoescape on %}{{ plugin.short_description }}{% endautoescape %}</td>
				<td>{{ plugin.score }} ({{ plugin.num_vote }} ratings)</td>
				<td>
					{% if plugin.url %}<a href="{{ plugin.url }}">doc</a>{% endif %}
					{% if plugin.git_repo %}<a href="{% autoescape on %}{{ plugin.git_repo }}{% endautoescape %} ">git</a>{% endif %}
				</td>
			</tr>
		{% endfor %}
	</table>
{% else %}
	<div class="error no-item-on-page">
		Sorry, no plugins published at the moment.
	</div>
{% endif %}
{% endblock %}
