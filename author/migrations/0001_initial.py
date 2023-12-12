# Generated by Django 5.0 on 2023-12-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('born_to', models.DateTimeField(null=True)),
                ('nickname', models.CharField(max_length=40)),
            ],
        ),
    ]
