# Generated by Django 2.2.5 on 2019-10-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(default='alex', max_length=60),
            preserve_default=False,
        ),
    ]
