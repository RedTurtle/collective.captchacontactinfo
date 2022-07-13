# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

#Plone
from plone.app.testing import TEST_USER_NAME, TEST_USER_ID
from plone.app.testing import login, logout
from plone.app.testing import setRoles
from plone.testing.z2 import Browser

from Acquisition import aq_base
from zope.component import getSiteManager
from Products.CMFPlone.tests.utils import MockMailHost
from Products.MailHost.interfaces import IMailHost
import transaction

from collective.captchacontactinfo.testing import (
    COLLECTIVE_CAPTCHACONTACTINFO_FUNCTIONAL_TESTING,
)


class TestContactInfo(unittest.TestCase):
    layer = COLLECTIVE_CAPTCHACONTACTINFO_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.portal._original_MailHost = self.portal.MailHost
        self.portal.MailHost = mailhost = MockMailHost('MailHost')
        
        # set up mail host
        sm = getSiteManager(context=self.portal)
        
        sm.unregisterUtility(provided=IMailHost)
        sm.registerUtility(mailhost, provided=IMailHost)
        
        # Set up browser
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            'Authorization',
            'Basic {username}:{password}'.format(
                username=SITE_OWNER_NAME,
                password=SITE_OWNER_PASSWORD),
        )