# Generated by Django 3.0.3 on 2020-06-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20200626_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='poll_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='poll_third_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='poll_two_count',
            field=models.IntegerField(default=0),
        ),
    ]
