from zope.interface import Interface
from zope import schema
from zope.formlib import form
from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.form import ControlPanelForm
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _


class IContactInfoPolicyForm(Interface):

    policy_page = schema.TextLine(title=_("contactinfo-config-policy",
                                          default=u"Policy page"),
                                description=_("contactinfo-config-policyhelp",
                                              default=u"Insert the path for the Page used for Policy text. For example: folder-a/policy-page"),
                                required=True)


class ContactInfoPolicyControlPanelAdapter(object):

    __sheet_id__ = 'contactinfo_properties'

    def __init__(self, context):
        super(ContactInfoPolicyControlPanelAdapter, self).__init__(context)
        self.context = context
        self.sheet = self.getSheet()

    def getSheet(self):
        '''
        Get the plone sheet containing the site properties
        '''
        pp = getToolByName(self.context, 'portal_properties')
        return getattr(pp, self.__sheet_id__, None)

    def get_policy_page(self):
        if not self.sheet:
            return ''
        value = self.sheet.getProperty('policy_page', '')
        return value

    def set_policy_page(self, value):
        if not self.sheet:
            return ''
        return self.sheet.manage_changeProperties(policy_page=value)
    policy_page = property(get_policy_page, set_policy_page)


class ContactInfoPolicyControlPanel(ControlPanelForm):

    form_fields = form.FormFields(IContactInfoPolicyForm)
    label = _(u"Contact-info Configuration")
    description = _(u"")
    form_name = _("Contact-info settings")

