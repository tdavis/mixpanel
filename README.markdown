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
requests to mixpanel. Instead, it queues them to a [beanstalkd][3] server, a very
fast and efficient in-memory queue. The daemon script issues requests at its
leisure.


Installation (short)
====================

If you have *none* of the above prerequisites and wish to run `beanstalkd` on
the same server as `mixpaneld` and log from there, this is the fastest
installation and setup possible. At console, execute:

	sudo easy_install mixpanel
	# For CentOS / RHEL, you need epel-release
	sudo rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/i386/epel-release-5-3.noarch.rpm
	sudo yum install beanstalkd
	beanstalkd -d
    mixpaneld -d

You are now up and running; you may skip down to "Usage".


Installation (long)
===================

Step 1:
-------

    easy_install mixpanel

or...

	git clone git://github.com/tdavis/mixpanel.git
	cd mixpanel
	python setup.py install

Step 2:
-------

You will need to run the `mixpaneld` script found at `scripts/mixpaneld`; the
script should already be in your `PATH` if you used `setup.py` (run
`which mixpaneld` to find out). Note that you may move it wherever you like.
The daemon takes optional parameters which you should view before running it by
using the command `mixpaneld --help`.

You will also need to have a running [beanstalkd][3] server. Installing and
setting up the server is quite trivial and is left as an exercise to the
reader; see the [beanstalkd download page][4]. Note that you do __not__ need a
client library; that is taken care of by this package.


Usage
=====

To queue a log call:

	from mixpanel import MixpanelLogger
	# Your mixpanel project code
	pcode = '7fdec37db628e57465b98e235338049d'
    # Beanstalk connection info
    host = 'localhost'
    port = 11311
	logger = MixpanelLogger(pcode, host, port)
	logger.log(
		category = 'my_category',
		action = 'my_action',
		# type, setting, distinct_value, etc.
	)

You may also set the following environment variables:

*   `MIXPANEL_PROJECT_CODE`: Your project code
*   `MIXPANEL_BEANSTALKD_HOST`: Default beanstalkd host
*   `MIXPANEL_BEANSTALKD_PORT`: Default beanstalkd port

The latter two have defaults, which happen to the be same defaults that
beanstalkd uses if you do not specify them when running the server. For this
reason, you can do what we saw above in `Installation (short)` to get things
running:

    beanstalkd -d
    mixpaneld -d

Then, in code:
    
    logger = MixpanelLogger(pcode)

And you're ready for logging in 3 lines without having to specify any host or
port information! The only downside is, this setup won't work cross-network.
For that, you'd need to specify LAN hosts when starting / connecting to the
daemons.

For a list of all possible keyword arguments to the mixpanel API, see the
[mixpanel API docs][5].


[1]: http://mixpanel.com
[2]: http://github.com/earl/beanstalkc/tree/master
[3]: http://xph.us/software/beanstalkd/
[4]: http://xph.us/software/beanstalkd/download.html
[5]: http://mixpanel.com/api/specification/

