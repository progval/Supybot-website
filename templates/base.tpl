{% load i18n %}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" >
	<head>
		<title>{% block title %}Supybot website{% endblock %}</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link rel="stylesheet" media="screen" type="text/css" href="/static/design.css" />
		{% block extrahead %}
		{% endblock %}
	</head>
<body>
	<div id="header">
		<a href="/"><img src="/static/logo.png" alt="logo" /></a>
		<br />
		Supybot website
		<div style="clear: both"></div>
	</div>
	<ul id="menu">
		<li><a href="{% url root_home %}">Home</a></li>
		<li><a href="{% url news_index %}">News</a></li>
		<li><a href="/doc/">Documentation</a></li>
		<li><a href="{% url get_index %}">Get Supybot</a></li>
		<li><a href="{% url plugins_index %}">Plugins</a></li>
		<li><a href="{% url users_index %}">Your account</a></li>
		<li><a href="{% url dpaste_snippet_new %}">Dpaste</a></li>
		<li><a href="{% url haystack_search %}">Search</a></li>
		<li><a href="{% url root_about %}">About</a></li>
	</ul>
	<div id="body">
		{% block body %}
		{% endblock %}
	</div>
</body>
</html>
