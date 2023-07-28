# -*- coding: utf-8 -*-


from Products.CMFPlone.browser.contact_info import ContactForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _
from z3c.form.interfaces import HIDDEN_MODE
import logging
import warnings
import z3c.form.field
import zope.schema

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
