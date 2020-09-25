# Generated by Django 3.0.3 on 2020-06-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('poll_one', models.CharField(blank=True, max_length=500, null=True)),
                ('poll_two', models.CharField(blank=True, max_length=500, null=True)),
                ('poll_third', models.CharField(blank=True, max_length=500, null=True)),
                ('poll_one_count', models.IntegerField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]