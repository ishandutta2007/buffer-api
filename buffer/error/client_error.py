class ClientError(Exception):

    """ClientError is used when the API returns an error"""

    def __init__(self, message, code):
        super(ClientError, self).__init__(message)
        self.message = message
        self.code = code
