# Generated by Django 3.1.5 on 2022-04-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSAdmin', '0003_auto_20220427_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Branch',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
