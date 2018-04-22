=====
polls
=====


Quick start
-----------

1. Add "plls" to your INSTALLED_APPS setting like this:
	
	INSTALLED_APPS = [
		...
		polls,
	]

2. Include the polls URLconf in your project urls.py like this::

	path('polls', include('polls.urls')),

3. Run `python manage.py migrate` to creat the polls model.

4. Start the develop server and visit http://127.0.0.1:8080/admin/ 
   to create a poll ( you'll need the admin app enabled).

5. Visit http://127.0.0.1:8080 to participate in the poll.

