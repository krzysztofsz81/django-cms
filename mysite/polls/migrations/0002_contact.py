# Generated by Django 2.2.5 on 2019-10-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
    ]
