Overview
========

This aptly-named module is a way to do scalable logging to [mixpanel][1]. It
makes use of the [beanstalkc][2] library (install handled by setuptools if you
don't have it) and requires a running [beanstalkd][3] server. The work flow is
quite simple: Use this module's client in your code to queue API requests.
The module's server will retrieve queued items and act on them. Simple.


Why So Complicated?
===================

Admittedly, this simple module comes with a lot of dependencies. Since it is
built with scalability and asynchrony in mind, it doesn't immediately send your
requests to mixpanel. Instead, it queues it to a [beanstalkd][3] server, a very
fast and efficient in-memory queue. The daemon script issues requests at its
leisure.


Installation
============

Step 1:
-------

`easy_install mixpanel` or...

	git clone git://github.com/tdavis/mixpanel.git
	cd mixpanel
	python setup.py install

Step 2:
-------

You will need to run the `mixpaneld` script found at `scripts/mixpaneld`; this
script was installed to your `PYTHON_PATH` if you used easy_install. Note that
you may move it wherever you like. The daemon takes optional parameters common
to such a daemon which may be viewed by running `mixpaneld --help`.

You will also need to have a running [beanstalkd][3] server. Installing and
setting up the server is quite trivial and is left as an exercise to the
reader; see the [beanstalkd download page][4]. Note that you do __not__ need a
client library; that is taken care of by this package.


Usage
=====

Remember, __first run `scripts/mixpaneld` as noted in the above section!__

To queue a log call:

	from mixpanel import MixPanelLogger
	"""
	Your mixpanel project code; set the environment variable
	MIXPANEL_PROJECT_CODE to keep from having to enter this again. Note that
	passed codes always take precedence!
	"""
	pcode = '7fdec37db628e57465b98e235338049d'
	logger = MixPanelLogger(pcode)
	logger.log(
		category = 'my_category',
		action = 'my_action',
		# type, setting, distinct_value, etc.
	)

For a list of all possible keyword arguments, see the [mixpanel API docs][5].


[1]: http://mixpanel.com
[2]: http://github.com/earl/beanstalkc/tree/master
[3]: http://xph.us/software/beanstalkd/
[4]: http://xph.us/software/beanstalkd/download.html
[5]: http://mixpanel.com/api/specification/

