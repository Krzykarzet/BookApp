# Generated by Django 2.2.1 on 2019-05-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20190515_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]