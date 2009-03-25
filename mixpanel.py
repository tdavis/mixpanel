import os, beanstalkc, cPickle

class MixPanelLogger(object):
    """
    The mixpanel logger client which communicates with the beanstalkd server.
    """
    #The beanstalk tube to use; you don't need to change this.
    tube = 'mixpanel'

    def __init__(self, pcode=None, host='0.0.0.0', port=11300):
        """
        Initialize logger.

        @param pcode: A valid project code; alpha-numeric, 32-byte string.
        @param host: beanstalkd host
        @param port: beanstalkd port
        """
        if not pcode:
            pcode = os.environ.get('MIXPANEL_PROJECT_CODE', None)
            if not pcode:
                raise ValueError, 'You did not supply a project code or env var'
        host = os.environ.get('MIXPANEL_BEANSTALKD_HOST', None) or host
        port = int(os.environ.get('MIXPANEL_BEANSTALKD_PORT', None) or port)
        self.conn = beanstalkc.Connection(host=host, port=port)
        self.conn.use(self.tube)
        self.pcode = pcode

    def log(self, **kwargs):
        """
        Log something to mixpanel.

        @param kwargs: Keyword arguments for API call. For a list see 
            http://mixpanel.com/api/specification/
        @returns: Aggregate number of total jobs
        """
        cat = kwargs.get('category', None)
        if not cat:
            raise KeyError, 'A valid category is required.'
        kwargs.update({'project': self.pcode})
        if 'value' in kwargs:
            kwargs['value'] = int(kwargs['value'])
        dump = cPickle.dumps(kwargs, cPickle.HIGHEST_PROTOCOL)
        return self.conn.put(dump)

