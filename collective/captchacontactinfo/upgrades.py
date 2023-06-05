# -*- coding: utf-8 -*-
from plone import api


default_profile = "profile-collective.captchacontactinfo:default"


def migrate_to_1100(context):
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runImportStepFromProfile(default_profile, "plone.app.registry")
