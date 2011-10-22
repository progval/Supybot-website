{% extends "base.tpl" %}

{% block body %}
<div id="profile">
	<h1>Profile</h1>
	<table id="summary">
		<tr>
			<td>Your username:</td>
			<td>{{ username }}</td>
		</tr>
		<tr>
			<td>Your avatar:<br />You can set it at <a href="https://www.libravatar.org/">Libravatar.org</a>.</td>
			<td><img src="{{ avatar }}" alt="avatar" /></td>
		</tr>
		<tr>
			<td>Your E-Mail address:</td>
			<td>{{ email }}</td>
		</tr>
		<tr>
			<td colspan="2" class="rowspan">
				<a href="{% url users_logout %}">Logout</a>
			</td>
		</tr>
	</table>
</div>
{% endblock %}
