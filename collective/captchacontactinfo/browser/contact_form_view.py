# -*- coding: utf-8 -*-
from Products.CMFPlone.browser.contact_info import ContactForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema

from Products.CMFPlone import PloneMessageFactory as _
from collective.captchacontactinfo import captchacontactinfoMessageFactory as _C
from Products.CMFPlone.browser.interfaces import IContactForm

import logging
import z3c.form.field
from Acquisition import aq_inner
from plone.formwidget.recaptcha.widget import ReCaptchaFieldWidget
from z3c.form import button
from z3c.form import field
from zope import interface
from zope.component import getMultiAdapter
from Products.statusmessages.interfaces import IStatusMessage

log = logging.getLogger(__name__)


class IReCaptchaForm(interface.Interface):

    captcha = schema.TextLine(
        title=u"ReCaptcha",
        description=u"",
        required=False
    )


class ReCaptcha(object):
    subject = u""
    captcha = u""

    def __init__(self, context):
        self.context = context


class ContactInfoPolicy(ContactForm):

    template = ViewPageTemplateFile('templates/contact-info.pt')
    schema = IContactForm
    ignoreContext = True
    success = False

    def updateFields(self):
        super(ContactInfoPolicy, self).updateFields()

        fields = field.Fields(IReCaptchaForm)
        fields['captcha'].widgetFactory = ReCaptchaFieldWidget
        fields_objects = z3c.form.field.Fields(fields)
        self.fields['sender_fullname'].field.required = False
        self.fields['sender_from_address'].field.required = False
        help_message = _C(
            u'help_sender_from_address_customized',
            default=u'Please enter your e-mail address if '
            'you want to receive an answer')
        self.fields['sender_from_address'].field.description = self.context.\
            translate(help_message)
        self.fields += fields_objects

    @button.buttonAndHandler(_(u'label_send', default='Send'), name='send')
    def handle_send(self, action):
        data, errors = self.extractData()
        if errors:
            IStatusMessage(self.request).add(
                self.formErrorsMessage,
                type=u'error'
            )

            return

        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request),
            name='recaptcha'
        )

        if captcha.verify():
            IStatusMessage(self.request).add(_(u'ReCaptcha validation passed.'))

        else:
            IStatusMessage(self.request).add(
                self.formErrorsMessage,
                type=u'The code you entered was wrong, '
                     'please enter the new one.'
            )
            return

        self.send_message(data)
        self.send_feedback()
        self.success = True
