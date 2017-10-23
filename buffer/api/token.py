class Token(object):

    """Returns api instance to get an access token.
    """

    _AUTH_URI = ("https://bufferapp.com/oauth2/authorize?" +
                 "client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

    def __init__(self, redirect_uri, client):
        """

        Args:
            redirect_uri: application redirect URI
            client: HTTPClient instance
        """
        self.client = client
        self._token = None
        self._redirect_uri = redirect_uri

    def request_token(self, code, options=None):

        """Returns an object with the authentication token for an account.

        '/oauth2/token' POST raw

        Args:
            code: authentication code obtained after Buffer api redirect from Token.get_auth_reditect_uri().
            options:
        """
        if not options:
            options = {}
        options['request_type'] = "raw"
        body = options['query'] if 'query' in options else {}
        body['redirect_uri'] = self.redirect_uri
        body['code'] = code
        body['grant_type'] = "authorization_code"
        body['client_id'] = self.client.auth.auth['client_id']
        body['client_secret'] = self.client.auth.auth['client_secret']

        response = self.client.post('/oauth2/token', body, options)
        self._token = response.body.get('access_token')

        return response

    @property
    def redirect_uri(self):

        """Returns an application redirect URI.
        """
        return self._redirect_uri

    @property
    def token(self):

        """Returns an account access token or None when not initialized or request failure.
        """
        return self._token

    def get_auth_redirect_uri(self, client_id):

        """Returns a redirect URI to obtain the code for token API request.
        """
        return self._AUTH_URI.format(client_id=client_id, redirect_uri=self.redirect_uri)
