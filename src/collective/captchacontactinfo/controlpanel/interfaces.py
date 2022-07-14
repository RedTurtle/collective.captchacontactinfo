# -*- coding: utf-8 -*-
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from collective.captchacontactinfo import captchacontactinfoMessageFactory as _


bot_prevention_vocabulary = SimpleVocabulary(
    [
        SimpleTerm(value="recaptcha", title=_("reCAPTCHA")),
        SimpleTerm(value="honeypot", title=_("Honeypot")),
    ]
)


class ICollectiveCaptchaContactInfoSettings(Interface):
    """Settings used in the control panel for default settings"""

    policy_page = schema.TextLine(
        title=_("contactinfo-config-policy", default="Policy page"),
        description=_(
            "contactinfo-config-policyhelp",
            default="Insert the path for the Page used for Policy text. For example: folder-a/policy-page",
        ),
        required=False,
    )

    bot_prevention_tecnique = schema.Choice(
        title=_("Bot prevention tecnique"),
        vocabulary=bot_prevention_vocabulary,
        required=True,
    )
