# -*- coding: utf-8 -*-
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope import schema

from collective.captchacontactinfo.controlpanel.interfaces import (
    ICollectiveCaptchaContactInfoSettings,
)
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _
from Products.CMFPlone.browser.interfaces import IContactForm

import logging
import z3c.form.field
from Acquisition import aq_inner
from plone.formwidget.recaptcha.widget import ReCaptchaFieldWidget
from z3c.form import button
from z3c.form import field
from zope import interface, schema
from zope.component import getMultiAdapter
from Products.statusmessages.interfaces import IStatusMessage


log = logging.getLogger(__name__)


class IReCaptchaForm(interface.Interface):

    captcha = schema.TextLine(title="ReCaptcha", description="", required=False)


class IHoneyPotForm(interface.Interface):
    """Interface defines honeypot fields"""

    confirm_email = schema.TextLine(
        title=_("Confirm email"), description=_("Confirm your email"), required=False
    )


class ReCaptcha(object):
    subject = ""
    captcha = ""

    def __init__(self, context):
        self.context = context


class ContactInfoPolicy(ContactForm):
    template = ViewPageTemplateFile("templates/contact-info.pt")
    schema = IContactForm
    ignoreContext = True
    success = False

    def __init__(self, *args, **kwargs):
        super(ContactInfoPolicy, self).__init__(*args, **kwargs)

        self.bot_prevention_tecnique = api.portal.get_registry_record(
            interface=ICollectiveCaptchaContactInfoSettings,
            name="bot_prevention_tecnique",
        )

    def updateFields(self):
        super(ContactInfoPolicy, self).updateFields()
        if "recaptcha" == self.bot_prevention_tecnique:
            fields = field.Fields(IReCaptchaForm)
            fields["captcha"].widgetFactory = ReCaptchaFieldWidget

        # default bahavior is Honeypot
        else:
            fields = field.Fields(IHoneyPotForm)

        fields_objects = z3c.form.field.Fields(fields)
        self.fields["sender_fullname"].field.required = False
        self.fields["sender_from_address"].field.required = False
        help_message = _(
            "help_sender_from_address_customized",
            default="Please enter your e-mail address if "
            "you want to receive an answer",
        )
        self.fields["sender_from_address"].field.description = self.context.translate(
            help_message
        )
        self.fields += fields_objects

    @button.buttonAndHandler(_("label_send", default="Send"), name="send")
    def handle_send(self, action):
        data, errors = self.extractData()
        if errors:
            IStatusMessage(self.request).add(self.formErrorsMessage, type="error")

            return

        if "recaptcha" == self.bot_prevention_tecnique:
            captcha = getMultiAdapter(
                (aq_inner(self.context), self.request), name="recaptcha"
            )

            if not captcha.verify():
                IStatusMessage(self.request).add(
                    _(
                        "not_compile_captcha",
                        default="The code you entered was wrong, please enter the new one.",
                    ),
                    type="error",
                )
                return

        # check if Honeypot was compiled by bot
        else:
            if data["confirm_email"]:
                IStatusMessage(self.request).add(
                    _(
                        "bad_field_value",
                        default=_(
                            "The value is not correct. If the problem persists, please contact the site administrator"
                        ),
                    ),
                    type="error",
                )
                return

        self.send_message(data)
        self.send_feedback()
        self.success = True
