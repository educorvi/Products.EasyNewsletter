# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import (
    ControlPanelFormWrapper,
    RegistryEditForm,
)
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from Products.EasyNewsletter import _
from Products.EasyNewsletter.interfaces import IProductsEasyNewsletterLayer
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IEasyNewsletterControlPanel(Interface):

    delivery_service_name = schema.TextLine(
        title=_(
            u'Delivery Service Name',
        ),
        description=_(
            u'Delivery service to be used. Can be either "mailhost" (default), "mailhost2" to use an alternative Mailhost with the data below or a custom utility providing IMailHost.',
        ),
        default=u'mailhost',
        required=True,
    )

    smtp_host = schema.TextLine(
        title=_(
            "SMTP Host",
        ),
        description=_(
            "The address of your local SMTP (outgoing e-mail) server. Usually 'localhost', unless you use an external server to send e-mail.",
        ),
        default="localhost",
        required=False,
    )

    smtp_port = schema.Int(
        title=_(
            "SMTP port",
        ),
        description=_(
            "The port of your local SMTP (outgoing e-mail) server. Usually '25'.",
        ),
        default=25,
        required=False,
    )

    smtp_userid = schema.TextLine(
        title=_(
            "ESMTP username",
        ),
        description=_(
            "SMTP username to be used instead of the Plone SMTP username",
        ),
        default="",
        required=False,
    )

    smtp_password = schema.Password(
        title=_(
            "ESMTP password",
        ),
        description=_(
            "SMTP password to be used instead of the Plone SMTP password",
        ),
        default="",
        required=False,
    )


class EasyNewsletterControlPanel(RegistryEditForm):
    schema = IEasyNewsletterControlPanel
    schema_prefix = "Products.EasyNewsletter.easy_newsletter_control_panel"
    label = _("Easy Newsletter Control Panel")


EasyNewsletterControlPanelView = layout.wrap_form(
    EasyNewsletterControlPanel, ControlPanelFormWrapper
)


@adapter(Interface, IProductsEasyNewsletterLayer)
class EasyNewsletterControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IEasyNewsletterControlPanel
    configlet_id = "easy_newsletter_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Easy Newsletter Control Panel")
    group = ""
    schema_prefix = "Products.EasyNewsletter.easy_newsletter_control_panel"
