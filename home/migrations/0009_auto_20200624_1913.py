# Generated by Django 3.0.4 on 2020-06-24 19:13

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
