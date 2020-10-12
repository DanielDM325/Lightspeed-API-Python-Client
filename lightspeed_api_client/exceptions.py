class RateLimitError(Exception):

    def __init__():
        self.message = 'RateLimitError: The user has sent too many requests in a given amount of time. Server returned 429 status code'

    def __str__(self):
        return self.message
