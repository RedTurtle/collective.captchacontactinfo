# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.CMFPlone.browser.interfaces import IContactForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from zope.component import getMultiAdapter
import zope.schema
import z3c.form.field
from z3c.form.interfaces import HIDDEN_MODE


import logging
import warnings

log = logging.getLogger(__name__)


class ContactInfoPolicy(ContactForm):

    template = ViewPageTemplateFile("templates/contact-info.pt")

    def updateFields(self):

        super(ContactInfoPolicy, self).updateFields()

        self.fields["sender_fullname"].field.required = False
        self.fields["sender_from_address"].field.required = False
        help_message = _(
            u"help_sender_from_address_customized",
            default=u"Please enter your e-mail address if "
            "you want to receive an answer",
        )
        self.fields["sender_from_address"].field.description = self.context.translate(
            help_message
        )

        schema_url_field = zope.schema.TextLine(
            __name__="starting_url",
            required=False,
        )
        orig_url_field = z3c.form.field.Fields(schema_url_field)
        self.fields += z3c.form.field.Fields(orig_url_field)

        self.fields["starting_url"].field.default = unicode(
            self.request.environ.get("HTTP_REFERER")
        )
        self.fields["starting_url"].mode = HIDDEN_MODE

    def generate_mail(self, variables, encoding=None):
        template = self.context.restrictedTraverse(self.template_mailview)
        result = template(self.context, **variables)
        if encoding is not None:
            # Maybe someone has customized 'send_message'
            # and still expects to get an encoded answer back.
            warnings.warn(
                "Calling generate_mail with an encoding argument is deprecated. "
                "You can leave it out, and get text (string) as result.",
                DeprecationWarning,
            )
            result = result.encode(encoding)
        return result
