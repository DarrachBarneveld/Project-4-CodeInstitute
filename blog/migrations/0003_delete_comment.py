# Generated by Django 3.2.20 on 2023-08-23 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_excerpt'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]