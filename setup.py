from setuptools import setup
import os

setup (
    name = 'mixpanel',
    version = '0.2',
    description = 'Small Python library to make calls to mixpanel\'s API. Requires beanstalkd server.',
    long_description = """
    This library includes a client and a server. The client is used to queue
    requests which will be made to mixpanel's API. The server daemon pulls the
    queued items out and sends the requests. Both require a running beanstalkd
    server. You can get beanstalkd from http://xph.us/software/beanstalkd/.
    """,
    author = 'Tom Davis',
    author_email = 'binjured@gmail.com',
    url = 'http://github.com/tdavis/mixpanel/tree/master',
    download_url = 'http://cloud.github.com/downloads/tdavis/mixpanel/mixpanel-0.2.tar.gz',
    classifiers = [ 'Development Status :: 4 - Beta',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: Python',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                  ],
    platforms = ['Any',],
    keywords = ['mixpanel',],
    packages = ['mixpanel',],
    package_dir = {'mixpanel': '.'},
    scripts = ['scripts/mixpaneld',],
    # beanstalkc: beanstalkd client library
    # daemon: script used to daemonize mixpaneld script
    install_requires=['beanstalkc', 'daemon>=1.0.1']
)

