# Generated by Django 2.2.1 on 2019-06-03 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190604_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30, null=True)),
                ('first_reg', models.DateField()),
                ('price', models.IntegerField()),
                ('fuel', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='description',
            new_name='dsc',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='car',
            name='sell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Sell'),
        ),
    ]
