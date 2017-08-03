class Profile(object):

    """Returns a social media profile api instance.

    Args:
        id: Identifier of a social media profile
    """

    def __init__(self, id, client):
        self.id = id
        self.client = client

    def show(self, options=None):
        """Returns details of the single specified social media profile.

        '/profiles/:id' GET
        """
        if not options:
            options = {}
            
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/profiles/' + self.id + '', body, options)

        return response

    def pending(self, options=None):
        """Returns an array of updates that are currently in the buffer for an individual social media profile.

        '/profiles/:id/updates/pending' GET
        """
        if not options:
            options = {}

        body = options['query'] if 'query' in options else {}

        response = self.client.get('/profiles/' + self.id + '/updates/pending', body, options)

        return response

    def sent(self, options=None):
        """Returns an array of updates that have been sent from the buffer for an individual social media profile.

        '/profiles/:id/updates/sent' GET
        """
        if not options:
            options = {}

        body = options['query'] if 'query' in options else {}

        response = self.client.get('/profiles/' + self.id + '/updates/sent', body, options)

        return response

    def reorder(self, order, options=None):
        """Edit the order at which statuses for the specified social media profile will be sent out of the buffer.

        '/profiles/:id/updates/reorder' POST

        Args:
            order: An ordered array of status update id's. This can be a partial array in combination with the offset parameter or a full array of every update in the profiles Buffer.
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}
        body['order'] = order

        response = self.client.post('/profiles/' + self.id + '/updates/reorder', body, options)

        return response

    def shuffle(self, options=None):
        """Randomize the order at which statuses for the specified social media profile will be sent out of the buffer.

        '/profiles/:id/updates/shuffle' POST
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}

        response = self.client.post('/profiles/' + self.id + '/updates/shuffle', body, options)

        return response

