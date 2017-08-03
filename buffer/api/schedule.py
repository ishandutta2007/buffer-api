class Schedule(object):

    """Returns scheduling api instance for social media profile.

    Args:
        id: Identifier of a social media profile
    """

    def __init__(self, id, client):
        self.id = id
        self.client = client

    def list(self, options=None):
        """Returns details of the posting schedules associated with a social media profile.

        '/profiles/:id/schedules' GET
        """
        if not options:
            options = {}

        body = options['query'] if 'query' in options else {}

        response = self.client.get('/profiles/' + self.id + '/schedules', body, options)

        return response

    def update(self, schedules, options=None):
        """Set the posting schedules for the specified social media profile.

        '/profiles/:id/schedules/update' POST

        Args:
            schedules: Each item in the array is an individual posting schedule which consists of days and times to match the format return by the above method.
        """
        if not options:
            options = {}

        body = options['body'] if 'body' in options else {}
        body['schedules'] = schedules

        response = self.client.post('/profiles/' + self.id + '/schedules/update', body, options)

        return response

