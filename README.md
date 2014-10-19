What is it?
===========

This website is not a CMS. It is not intended to be deployed by everyone.
Only one instance. The "official" one.
However, libre software (aka FOSS) is the Good, and I don't want this website
to be lost if I loose all my data, or if I become unreachable.

The website deployed at http://supybot.aperio.fr/ uses this source code, with no
modification (only localsettings.py has been added).

How does it work?
=================

It's a source code. Code is the best documentation ever.

The only missing part of the source code is a file called localsettings.py.
You should define some variables in it, in order to get them imported by
settings.py (look at import statements in settings.py, it will give you
the list of variables).

First at all, the list of dependancies in the INSTALL file. As you can see,
it is based on Django and uses Sphinx for the doc.

The directories and applications
================================

In media/repositories/ are repositories the users register in order to
auto-import plugins from them. If you use Apache with WSGI, www-data should
have write access to this directory.
List of the applications:
* dpaste: A modified version of Dpaste, that announces the pastes on IRC
  (through a Supybot, of course!)
* get: Download links. Can be managed via the Django admin.
* news: The news application, with comments. Also managed via the Django
  admin.
* plugins: Plugins catalog. Auto-import from Git repositories. Comments and
  ratings system. Users can manage their own plugins.
* users: Application that handle user operations (registration, connection,
  disconnection).

The doc/ directory is a submodule that contains a Sphinx documentation. You
need to use `make html` to generate it.
