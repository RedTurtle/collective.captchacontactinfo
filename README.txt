Introduction
============
A simple Plone customization for the "*Contact form*" form that add a captcha regognition for anonymous users.

When anonymous try to use contact-info form, they *must* provide also a captcha protection
value.

Form protection
===============

The captcha protection is given by the `collective.recaptcha`__ product.

__ http://pypi.python.org/pypi/collective.recaptcha


Policy text
===========

To show a policy text in contact-form, you just need to write it into a page in the portal, and then set his path in a property in ZMI: portal_properties/captchacontactinfo_properties or in plone-control-panel.

Dependencies
============

This product has been tested on Plone 3.3.5 (feedback on Plone 4 tests are welcome)

Credits
=======

Developed with the support of `Regione Emilia Romagna`__; Regione Emilia Romagna supports the `PloneGov initiative`__.

__ http://www.regione.emilia-romagna.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/
   
   