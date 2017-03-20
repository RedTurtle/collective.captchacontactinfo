# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'captchacontactinfo-various.txt',
        ]

def post_install(context):
    """Post install script"""
    if context.readDataFile('captchacontactinfo-various.txt') is None:
        return
    # Do something during the installation of this package

def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('captchacontactinfo-various.txt') is None:
        return
    # Do something during the uninstallation of this package




# from Products.CMFCore.utils import getToolByName
#
# def import_various(context):
#     if context.readDataFile('captchacontactinfo-various.txt') is None:
#         return
#     portal = context.getSite()
#     addPropertySheet(portal)
#
#
# def addPropertySheet(portal):
#     portal_properties = getToolByName(portal, 'portal_properties')
#     contactinfo_properties = getattr(portal_properties,
#                                      'contactinfo_properties',
#                                      None)
#     if not contactinfo_properties:
#         portal_properties.addPropertySheet(id='contactinfo_properties',
#                                            title='Contact Info properties')
#         portal.plone_log("Added contactinfo_properties property sheet")
#         contactinfo_properties = getattr(portal_properties, 'contactinfo_properties', None)
#     if not contactinfo_properties.hasProperty('policy_page'):
#         contactinfo_properties.manage_addProperty('policy_page', "", 'string')
