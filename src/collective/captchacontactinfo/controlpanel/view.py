# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from collective.captchacontactinfo.controlpanel.interfaces import (
    ICollectiveCaptchaContactInfoSettings,
)


class CollectiveCaptchaSettingsEditForm(controlpanel.RegistryEditForm):
    """settings form."""

    schema = ICollectiveCaptchaContactInfoSettings
    id = "CollectiveCaptchaSettingsEditForm"
    label = "Contact-info Configuration"
    description = ""


class CollectiveCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Analytics settings control panel."""

    form = CollectiveCaptchaSettingsEditForm
