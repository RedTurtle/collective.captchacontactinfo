from Products.Five.browser import BrowserView
from plone import api
from collective.captchacontactinfo.controlpanel.interfaces import ICollectiveCaptchaContactInfoSettings


class View(BrowserView):
    '''
    '''
    def __call__(self):
        '''

        '''
        policy_path = api.portal.get_registry_record(
            'policy_page',
            interface=ICollectiveCaptchaContactInfoSettings)

        if not policy_path:
            return ''

        policy_obj = api.content.get(path=str(policy_path))
        return policy_obj.text.output
