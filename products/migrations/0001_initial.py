# Generated by Django 3.1.5 on 2021-01-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
