# Generated by Django 4.0 on 2022-01-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fetchingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField()),
                ('iname', models.CharField(max_length=100)),
                ('iquantity', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
