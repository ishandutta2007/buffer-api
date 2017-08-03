class Update(object):

    """Returns a social media update api instance.

    Args:
        id: Identifier of a social media update
    """

    def __init__(self, id, client):
        self.id = id
        self.client = client

    def show(self, options=None):
        """Returns a single social media update.

        '/updates/:id' GET
        """
        if not options:
            options = {}
            
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/updates/' + self.id + '', body, options)

        return response

    def interactions(self, options=None):
        """Returns the detailed information on individual interactions with the social media update such as favorites, retweets and likes.

        '/updates/:id/interactions' GET
        """
        if not options:
            options = {}

        body = options['query'] if 'query' in options else {}

        response = self.client.get('/updates/' + self.id + '/interactions', body, options)

        return response

    def update(self, text, options=None):
        """Edit an existing, individual status update.

        '/updates/:id/update' POST

        Args:
            text: The status update text.
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}
        body['text'] = text

        response = self.client.post('/updates/' + self.id + '/update', body, options)

        return response

    def share(self, options=None):
        """Immediately shares a single pending update and recalculates times for updates remaining in the queue.

        '/updates/:id/share' POST
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}

        response = self.client.post('/updates/' + self.id + '/share', body, options)

        return response

    def destroy(self, options=None):
        """Permanently delete an existing status update.

        '/updates/:id/destroy' POST
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}

        response = self.client.post('/updates/' + self.id + '/destroy', body, options)

        return response

    def top(self, options=None):
        """Move an existing status update to the top of the queue and recalculate times for all updates in the queue. Returns the update with its new posting time.

        '/updates/:id/move_to_top' POST
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}

        response = self.client.post('/updates/' + self.id + '/move_to_top', body, options)

        return response

