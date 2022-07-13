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
    """Update registry and controlpanel to version 1001"""
    
    logger.info("Running upgrade 1001")

    update_registry(context)
    update_controlpanel(context)
