# Generated by Django 4.2.5 on 2023-09-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=100)),
                ('speciality', models.TextField()),
                ('idphoto', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]