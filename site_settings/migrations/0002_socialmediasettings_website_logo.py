# Generated by Django 3.0.4 on 2020-07-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='website_logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]