# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import collective.captchacontactinfo


class CollectiveCaptchacontactinfoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.captchacontactinfo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.captchacontactinfo:default")


COLLECTIVE_CAPTCHACONTACTINFO_FIXTURE = CollectiveCaptchacontactinfoLayer()


COLLECTIVE_CAPTCHACONTACTINFO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CAPTCHACONTACTINFO_FIXTURE,),
    name="CollectiveCaptchacontactinfoLayer:IntegrationTesting",
)


COLLECTIVE_CAPTCHACONTACTINFO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CAPTCHACONTACTINFO_FIXTURE,),
    name="CollectiveCaptchacontactinfoLayer:FunctionalTesting",
)


COLLECTIVE_CAPTCHACONTACTINFO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_CAPTCHACONTACTINFO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveCaptchacontactinfoLayer:AcceptanceTesting",
)
