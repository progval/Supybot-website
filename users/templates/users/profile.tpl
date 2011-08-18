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
			<td>Your E-Mail address:</td>
			<td>{{ email }}</td>
		</tr>
		<tr>
			<td colspan="2" class="rowspan">
				<a href="../logout/">Logout</a>
			</td>
		</tr>
	</table>
</div>
{% endblock %}
