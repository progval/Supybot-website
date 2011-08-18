{% extends "base.tpl" %}
{% load markup %}

{% block body %}
<div id="download_links">
	<h1>Download links</h1>
	{% if links %}
		<table>
			<tr>
				<th>Project</th>
				<th>Version</th>
				<th>Release notes</th>
				<th>Link type</th>
			</tr>
			{% for link in links %}
				<tr>
					<td>{{ link.project }}</td>
					<td>{{ link.version }}</td>
					<td>{{ link.release_notes|markdown:"safe" }}</td>
					<td><a href="{{ link.link }}">{{ link.type }}</a></td>
				</tr>
			{% endfor %}
		</table>
	{% else %}
		<div class="error no-item-on-page">
			Sorry, no download link at the moment.
		</div>
	{% endif %}
</div>
{% endblock %}
