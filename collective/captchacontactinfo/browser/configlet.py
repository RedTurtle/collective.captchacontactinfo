from zope.interface import Interface
from zope.component import adapts
from zope.interface import implements
from zope import schema
from zope.app.form import CustomWidgetFactory
from zope.app.form.browser import ObjectWidget
from zope.app.form.browser import ListSequenceWidget
from zope.formlib import form

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from Products.CMFPlone.interfaces import IPloneSiteRoot

from plone.app.controlpanel.form import ControlPanelForm


class IContactInfoPolicyForm(Interface):

    policy_page = schema.TextLine(title=u"Policy page",
                                description=u"Insert the path for the Page usced for Policy text. For example: folder-a/policy-page",
                                required=True)


class ContactInfoPolicyControlPanelAdapter(object):

    __sheet_id__ = 'captchacontactinfo_properties'

    def __init__(self, context):
        super(ContactInfoPolicyControlPanelAdapter, self).__init__(context)
        self.context = context
        self.sheet = self.getSheet()

    def getSheet(self):
        '''
        Get the plone sheet containing the site properties
        '''
        pp = getToolByName(self.context, 'portal_properties')
        return pp.get(self.__sheet_id__)

    def get_policy_page(self):
        value = self.sheet.getProperty('policy_page', '')
        return value

    def set_policy_page(self, value):
        return self.sheet.manage_changeProperties(policy_page=value)
    policy_page = property(get_policy_page, set_policy_page)


class ContactInfoPolicyControlPanel(ControlPanelForm):

    form_fields = form.FormFields(IContactInfoPolicyForm)
    label = "Captcha Contact Info Cofig"
    description = "This form is for managing news archive"
    form_name = "News archive settings"

