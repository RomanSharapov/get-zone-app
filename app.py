import requests
import falcon

zone_url = "http://metadata.google.internal/computeMetadata/v1/instance/zone"

cache = {}

class View(object):
    def on_get(self, req, resp):
        zone = cache.get('zone')
        if not zone:
            resp = requests.get(zone_url, headers={'Metadata-Flavor': 'Google'})
            zone = cache['zone'] = resp.text.split('/')[-1]
        resp.status = falcon.HTTP_200
        resp.body = f"Welcome to the torykube! You are being served from {zone}"

app = falcon.API()
app.add_route('/', View())
