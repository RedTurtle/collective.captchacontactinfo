Introduction
============

A simple Plone customization for the "*Contact form*" form that add a captcha regognition for anonymous users.

When anonymous try to use contact-info form, they *must* provide also a captcha protection
value.

Form protection
===============

The captcha protection is given by `collective.recaptcha`__ product.

__ http://pypi.python.org/pypi/collective.recaptcha

After installing this package, you must obtain a public and private key from
`http://recaptcha.net <http://recaptcha.net>`_, and configure them at http://path/to/site/@@recaptcha-settings

Policy text
===========

To show a policy text in contact-form, you just need to write it into a page in the portal, and
then set his path in a property in ZMI: portal_properties/captchacontactinfo_properties or in plone-control-panel:
http://path/to/site/@@contact-info-controlpanel
The title of the page will be shown in the form before the text.
It is also possible to provide a view name. In that case, a simple hyperlink to that view will be provided.

Translations
============

This product has been translated into

- English
- German
- Italian
- French

Dependencies
============

This product has been tested on Plone 3.3.5, Plone 4.2 and 4.3.

Credits
=======

Developed with the support of `Regione Emilia Romagna`__; Regione Emilia Romagna supports the `PloneGov initiative`__.

__ http://www.regione.emilia-romagna.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
