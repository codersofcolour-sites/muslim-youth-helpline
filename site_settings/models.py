from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.


@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for the site"""

    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    instagram = models.URLField(
        blank=True, null=True, help_text="Instagram URL")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("facebook"),
            FieldPanel("linkedin"),
        ], heading="Social Media Settings")
    ]
