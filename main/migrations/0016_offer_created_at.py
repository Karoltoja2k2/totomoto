# Generated by Django 2.2.1 on 2019-06-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190627_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
