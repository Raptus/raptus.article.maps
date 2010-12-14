from raptus.googlemaps.browser.api import Api as BaseApi
from raptus.article.maps.interfaces import IMap, IMaps
from zope.component import queryAdapter


class Api(BaseApi):
    """ This viewlet overrides the api-viewlet from raptus.googlemaps. With 
        the difference thats this viewlet is only rendered if some google-maps
        are available.
    """
    
    def render(self):
        if IMap.providedBy(self.context):
            return self.index()
        provider = queryAdapter(self.context, interface=IMaps)
        if provider and provider.getMaps():
            return self.index()
        return ''