from Products.CMFCore.utils import getToolByName

def import_various(context):
    if context.readDataFile('captchacontactinfo-various.txt') is None:
        return
    portal = context.getSite()
    addPropertySheet(portal)


def addPropertySheet(portal):
    portal_properties = getToolByName(portal, 'portal_properties')
    contactinfo_properties = getattr(portal_properties,
                                         'captchacontactinfo_properties',
                                         None)
    if not contactinfo_properties:
        portal_properties.addPropertySheet(id='contactinfo_properties',
                                           title='Contact Info properties')
        portal.plone_log("Added contact-info properties property-sheet")
        contactinfo_properties = getattr(portal_properties, 'contactinfo_properties', None)
    if not contactinfo_properties.hasProperty('policy_page'):
        contactinfo_properties.manage_addProperty('policy_page', "", 'string')
