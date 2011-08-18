{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<h1>
	Latest news
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
	<ul id="news_list">
		{% for news in page.object_list %}
			<li>
				<h2><a href="{% url news_read news.slug %}">{% autoescape on%}{{ news.title }}{% endautoescape %}</a></h2>
				{{ news.short_description|markdown:"safe" }}
			</li>
		{% endfor %}
	</ul>
{% else %}
	<div class="error no-item-on-page">
		Sorry, no news published at the moment.
	</div>
{% endif %}
{% endblock %}
