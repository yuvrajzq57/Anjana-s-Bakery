# Generated by Django 4.0.2 on 2022-02-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=123)),
                ('Address', models.CharField(default='', max_length=123)),
                ('Landmark', models.CharField(default='', max_length=123)),
                ('City', models.CharField(default='', max_length=123)),
                ('State', models.CharField(default='', max_length=123)),
                ('Zip', models.CharField(default='', max_length=123)),
            ],
        ),
    ]
