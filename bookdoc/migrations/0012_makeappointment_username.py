# Generated by Django 4.2.5 on 2023-09-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdoc', '0011_alter_makeappointment_appdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeappointment',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
