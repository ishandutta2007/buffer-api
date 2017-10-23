class Link(object):

    """Returns api instance to get information about links shared through Buffer.
    """

    def __init__(self, client):
        self.client = client

    def shares(self, url, options=None):
        """Returns an object with a the numbers of shares a link has had using Buffer.

        '/link/shares' GET

        Args:
            url: URL of the page for which the number of shares is requested.
            options:
        """
        options = {} if options is None else options
        body = options['query'] if 'query' in options else {}
        body['url'] = url

        response = self.client.get('/link/shares', body, options)

        return response

