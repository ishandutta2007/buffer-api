class User(object):

    """Returns authenticated user api instance.
    """

    def __init__(self, client):
        self.client = client

    def show(self, options=None):
        """Returns information about the authenticated user.

        '/user' GET
        """
        if not options:
            options = {}

        body = options['query'] if 'query' in options else {}

        response = self.client.get('/user', body, options)

        return response

    def profiles(self, options=None):
        """Returns an array of social media profiles connected to the authenticated users account.

        '/profiles' GET
        """
        if not options:
            options = {}

        body = options['query'] if 'query' in options else {}

        response = self.client.get('/profiles', body, options)

        return response

    def create_update(self, text, profile_ids, options=None):
        """Create one or more new status updates.

        '/updates/create' POST

        Args:
            text: The status update text.
            profile_ids: An array of profile id's that the status update should be sent to. Invalid profile_id's will be silently ignored.
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}
        body['text'] = text
        body['profile_ids'] = profile_ids

        response = self.client.post('/updates/create', body, options)

        return response

