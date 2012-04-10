from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from collective.captchacontactinfo.browser.interfaces import IContactinfoSupportView
from zope.interface import implements


class View(BrowserView):
    """
    A support view for contact-info form
    """
    implements(IContactinfoSupportView)

    def getPolicyText(self):
        """
        Return privacy-text from a page in the portal
        """
        portal_properties = getToolByName(self.context, 'portal_properties')
        contactinfo_properties = getattr(portal_properties,
                                         'contactinfo_properties',
                                         None)
        if not contactinfo_properties:
            return {}
        page_policy_path = contactinfo_properties.getProperty('policy_page', '').lstrip("/")
        if not page_policy_path:
            return {}
        if isinstance(page_policy_path, unicode):
            try:
                page_policy_path = page_policy_path.encode('utf-8')
            except:
                return {}
        portal_path = "/".join(self.context.portal_url.getPortalObject().getPhysicalPath())
        page_policy = self.context.restrictedTraverse("%s/%s" % (portal_path, page_policy_path), None)
        if not page_policy:
            return {}
        return {'title': page_policy.Title(), 'text': page_policy.getText()}
