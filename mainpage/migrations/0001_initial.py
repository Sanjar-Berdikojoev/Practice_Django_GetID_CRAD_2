# Generated by Django 4.1.3 on 2022-11-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PC_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('more_button', models.CharField(max_length=4)),
            ],
        ),
    ]