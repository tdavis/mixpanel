from setuptools import setup
import os

setup (
    name = 'mixpanel',
    version = '0.1',

    description = 'Small Python library to make calls to mixpanel\'s API. Requires beanstalkd server.',
    long_description = """
    This library includes a client and a server. The client is used to queue
    requests which will be made to mixpanel's API. The server daemon pulls the
    queued items out and sends the requests. Both require a running beanstalkd
    server. You can get beanstalkd from http://xph.us/software/beanstalkd/.
    """,

    author = 'Tom Davis',
    author_email = 'tom@ticketstumbler.com',

    url = 'http://github.com/tdavis/mixpanel/tree/master',
    #download_url = '',

    classifiers = [ 'Development Status :: 4 - Beta',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: Python',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                    ],

    platforms = ('Any',),
    keywords = ('mixpanel',),

    packages = ['mixpanel',],
    
    package_dir = {'': '.'},
    
    scripts = ['scripts/mixpaneld'],

    install_requires=['beanstalkc'],
    )

