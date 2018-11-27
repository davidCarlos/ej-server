# Generated by Django 2.1.3 on 2018-11-27 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ej_boards', '0002_add_slug_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='custom_domain',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Domínio invalido', regex='\\w{3}.?[a-z]+\\.[a-z]+')], verbose_name='Custom Domain'),
        ),
    ]
