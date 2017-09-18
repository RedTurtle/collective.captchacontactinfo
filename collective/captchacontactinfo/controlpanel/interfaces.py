# -*- coding: utf-8 -*-
from zope import schema
from zope.interface import Interface
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _


class ICollectiveCaptchaContactInfoSettings(Interface):
    """Settings used in the control panel for default settings
    """

    policy_page = schema.TextLine(title=_("contactinfo-config-policy",
                                          default=u"Policy page"),
                                description=_("contactinfo-config-policyhelp",
                                              default=u"Insert the path for the Page used for Policy text. For example: folder-a/policy-page"),
                                required=False)
