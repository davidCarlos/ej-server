# Generated by Django 2.0.7 on 2018-07-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ej_conversations', '0009_conversationboard'),
        ('ej_users', '0002_auto_20180529_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_conversations',
            field=models.ManyToManyField(to='ej_conversations.Conversation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]