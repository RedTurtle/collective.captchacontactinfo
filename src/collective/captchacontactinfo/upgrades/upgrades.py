from cmath import e
from plone import api
from collective.captchacontactinfo.controlpanel.interfaces import (
    ICollectiveCaptchaContactInfoSettings,
)

import logging


DEFAULT_PROFILE = "profile-collective.captchacontactinfo:default"

logger = logging.getLogger(__name__)


def update_profile(context, profile, run_dependencies=True):
    context.runImportStepFromProfile(DEFAULT_PROFILE, profile, run_dependencies)


def update_registry(context):
    update_profile(context, "plone.app.registry", run_dependencies=False)


def update_controlpanel(context):
    update_profile(context, "controlpanel")


def to_1001(context):
    """Update to version 1001 (`honeypot_settings` branch features)"""

    logger.info("Running upgrade 1001")

    update_registry(context)
    update_controlpanel(context)

    try:
        api.portal.set_registry_record(
            name="bot_prevention_tecnique",
            value="honeypot",
            interface=ICollectiveCaptchaContactInfoSettings,
        )
    except:
        logger.warning("Couldn't write to registry")
        return

    logger.info("Successful upgrade to 1001")
