# Generated by Django 2.1.3 on 2018-11-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ej_boards', '0002_add_slug_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='custom_domain',
            field=models.CharField(blank=True, max_length=50, verbose_name='Custom Domain'),
        ),
    ]
