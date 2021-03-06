# Generated by Django 2.1.2 on 2018-10-15 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ej_conversations', '0002_auto_20181015_1654'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ej_conversations.Comment')),
                ('promoter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='see_promotions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GivenPower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('data', picklefield.fields.PickledObjectField(editable=False)),
                ('is_exhausted', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ej_conversations.Conversation')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_ej_powers.givenpower_set+', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('timeframed', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='GivenBridgePower',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ej_powers.givenpower',),
            managers=[
                ('timeframed', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='GivenMinorityPower',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ej_powers.givenpower',),
            managers=[
                ('timeframed', django.db.models.manager.Manager()),
            ],
        ),
    ]
