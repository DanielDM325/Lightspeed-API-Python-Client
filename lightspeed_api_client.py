class LightspeedAPIClient:
    API_URL = 'https://api.webshopapp.com/nl/'
    API_key = ''
    API_secret = ''

    def __init__(self, API_key, API_secret):
        self.API_key = API_key
        self.API_secret = API_secret
