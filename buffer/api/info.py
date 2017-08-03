class Info(object):

    """Returns api instance to get auxilary information about Buffer useful when creating your app.
    """

    def __init__(self, client):
        self.client = client

    def show(self, options=None):
        """Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.

        '/info/configuration' GET
        """
        if not options:
            options = {}
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/info/configuration', body, options)

        return response

