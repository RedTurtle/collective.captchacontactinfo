# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.CMFPlone.browser.interfaces import IContactForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from zope.component import getMultiAdapter

import logging

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
