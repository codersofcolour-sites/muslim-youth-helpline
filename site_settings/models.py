from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.


@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for the site"""

    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    instagram = models.URLField(
        blank=True, null=True, help_text="Instagram URL")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")

    website_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        ImageChooserPanel('website_logo'),
        MultiFieldPanel([
            FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("facebook"),
            FieldPanel("linkedin"),
        ], heading="Site Settings")
    ]
