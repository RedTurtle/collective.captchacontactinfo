# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from collective.captchacontactinfo.testing import (  # noqa: E501
    COLLECTIVE_CAPTCHACONTACTINFO_INTEGRATION_TESTING,
)

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.captchacontactinfo is properly installed."""

    layer = COLLECTIVE_CAPTCHACONTACTINFO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.captchacontactinfo is installed."""
        self.assertTrue(
            self.installer.is_product_installed("collective.captchacontactinfo")
        )

    def test_browserlayer(self):
        """Test that ICollectiveCaptchacontactinfoLayer is registered."""
        from plone.browserlayer import utils

        from collective.captchacontactinfo.interfaces import (
            ICollectiveCaptchaContactInfoLayer,
        )

        self.assertIn(ICollectiveCaptchaContactInfoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_CAPTCHACONTACTINFO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.captchacontactinfo")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.captchacontactinfo is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("collective.captchacontactinfo")
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveCaptchacontactinfoLayer is removed."""
        from plone.browserlayer import utils

        from collective.captchacontactinfo.interfaces import (
            ICollectiveCaptchaContactInfoLayer,
        )

        self.assertNotIn(ICollectiveCaptchaContactInfoLayer, utils.registered_layers())
