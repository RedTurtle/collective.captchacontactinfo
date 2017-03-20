from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema
from Products.CMFPlone import PloneMessageFactory as _


class ICollectiveCaptchaContactInfoLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
