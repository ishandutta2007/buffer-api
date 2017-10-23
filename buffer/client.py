from .http_client import HttpClient

# Assign all the api classes
from .api.info import Info
from .api.user import User
from .api.link import Link
from .api.profile import Profile
from .api.schedule import Schedule
from .api.update import Update
from .api.token import Token

class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def info(self):
        """Returns api instance to get auxilary information about Buffer useful when creating your app.
        """
        return Info(self.http_client)

    def user(self):
        """Returns authenticated user api instance.
        """
        return User(self.http_client)

    def link(self):
        """Returns api instance to get information about links shared through Buffer.
        """
        return Link(self.http_client)

    def profile(self, id):
        """Returns a social media profile api instance.

        Args:
            id: Identifier of a social media profile
        """
        return Profile(id, self.http_client)

    def schedule(self, id):
        """Returns scheduling api instance for social media profile.

        Args:
            id: Identifier of a social media profile
        """
        return Schedule(id, self.http_client)

    def update(self, id):
        """Returns a social media update api instance.

        Args:
            id: Identifier of a social media update
        """
        return Update(id, self.http_client)

    def token(self, redirect_uri):
        """Returns a token request api.

        Args:
            redirect_uri: Application redirect URI
        """
        return Token(redirect_uri, self.http_client)
