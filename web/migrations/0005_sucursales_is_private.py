# Generated by Django 3.2.4 on 2022-04-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_sucursales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursales',
            name='is_private',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
