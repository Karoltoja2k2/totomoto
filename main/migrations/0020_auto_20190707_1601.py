# Generated by Django 2.2.1 on 2019-07-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_carmark_carmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='prod_year',
            field=models.IntegerField(null=True),
        ),
    ]
