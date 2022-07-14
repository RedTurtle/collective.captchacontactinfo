# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest
from unittest.mock import patch

# Plone
from plone.testing.z2 import Browser
from plone.formwidget.recaptcha.view import RecaptchaView
from plone import api

from Acquisition import aq_base
from zope.component import getSiteManager
from Products.CMFPlone.tests.utils import MockMailHost
from Products.MailHost.interfaces import IMailHost
import transaction

from collective.captchacontactinfo.controlpanel.interfaces import (
    ICollectiveCaptchaContactInfoSettings,
)
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings

from collective.captchacontactinfo.testing import (
    COLLECTIVE_CAPTCHACONTACTINFO_FUNCTIONAL_TESTING,
)


class TestContactInfo(unittest.TestCase):
    layer = COLLECTIVE_CAPTCHACONTACTINFO_FUNCTIONAL_TESTING

    def setUp(self):
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.portal._original_MailHost = self.portal.MailHost
        self.portal.MailHost = mailhost = MockMailHost("MailHost")

        api.portal.set_registry_record(
            "plone.email_from_address", "site_addr@plone.com"
        )
        api.portal.set_registry_record("plone.email_from_name", "Plone test site")

        sm = getSiteManager(context=self.portal)
        sm.unregisterUtility(provided=IMailHost)
        sm.registerUtility(mailhost, provided=IMailHost)

        transaction.commit()

        # Set up browser
        self.url = "{}/@@contact-info".format(self.portal.absolute_url())

    def tearDown(self):
        self.portal.MailHost = self.portal._original_MailHost
        sm = getSiteManager(context=self.portal)
        sm.unregisterUtility(provided=IMailHost)
        sm.registerUtility(aq_base(self.portal._original_MailHost), provided=IMailHost)

    def test_email_sent(self):
        browser = Browser(self.app)

        browser.open(self.url)
        browser.getControl(name="form.widgets.subject").value = "test"
        browser.getControl(name="form.buttons.send").click()

        self.assertEqual(browser.url, self.url)
        self.assertIn("A mail has now been sent", browser.contents)

        self.assertEqual(len(self.portal.MailHost.messages), 1)

    @patch.object(RecaptchaView, "verify")
    def test_captcha_negative(self, captcha_verify):
        browser = Browser(self.app)

        api.portal.set_registry_record(
            interface=ICollectiveCaptchaContactInfoSettings,
            name="bot_prevention_tecnique",
            value="recaptcha",
        )
        api.portal.set_registry_record(
            interface=IReCaptchaSettings, name="public_key", value="test"
        )
        api.portal.set_registry_record(
            interface=IReCaptchaSettings, name="private_key", value="test"
        )

        transaction.commit()

        # set up mock of captcha call
        captcha_verify.return_value = False

        browser.open(self.url)
        browser.getControl(name="form.widgets.subject").value = "test"
        browser.getControl(name="g-recaptcha-response").value = "bad_code"
        browser.getControl(name="form.buttons.send").click()

        self.assertIn("The code you entered was wrong", browser.contents)
        self.assertEqual(len(self.portal.MailHost.messages), 0)

    @patch.object(RecaptchaView, "verify")
    def test_captcha_positive(self, captcha_verify):
        browser = Browser(self.app)

        api.portal.set_registry_record(
            interface=ICollectiveCaptchaContactInfoSettings,
            name="bot_prevention_tecnique",
            value="recaptcha",
        )
        api.portal.set_registry_record(
            interface=IReCaptchaSettings, name="public_key", value="test"
        )
        api.portal.set_registry_record(
            interface=IReCaptchaSettings, name="private_key", value="test"
        )

        transaction.commit()

        # set up mock of captcha call
        captcha_verify.return_value = True

        browser.open(self.url)
        browser.getControl(name="form.widgets.subject").value = "test"
        browser.getControl(name="g-recaptcha-response").value = "good_code"
        browser.getControl(name="form.buttons.send").click()

        self.assertIn("A mail has now been sent", browser.contents)
        self.assertEqual(len(self.portal.MailHost.messages), 1)

    def test_honeypot_positive(self):
        browser = Browser(self.app)

        api.portal.set_registry_record(
            interface=ICollectiveCaptchaContactInfoSettings,
            name="bot_prevention_tecnique",
            value="honeypot",
        )

        transaction.commit()

        browser.open(self.url)
        browser.getControl(name="form.widgets.subject").value = "test"
        browser.getControl(name="form.buttons.send").click()

        self.assertIn("A mail has now been sent", browser.contents)
        self.assertEqual(len(self.portal.MailHost.messages), 1)

    def test_honeypot_negative(self):
        browser = Browser(self.app)

        api.portal.set_registry_record(
            interface=ICollectiveCaptchaContactInfoSettings,
            name="bot_prevention_tecnique",
            value="honeypot",
        )

        transaction.commit()

        browser.open(self.url)
        browser.getControl(name="form.widgets.subject").value = "test"

        # honeyport field
        browser.getControl(name="form.widgets.confirm_email").value = "test"
        browser.getControl(name="form.buttons.send").click()

        self.assertIn("The value is not correct", browser.contents)
        self.assertEqual(len(self.portal.MailHost.messages), 0)
