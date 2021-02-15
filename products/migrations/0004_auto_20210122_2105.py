# Generated by Django 3.1.5 on 2021-01-22 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210120_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_file',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default_product_image.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('In Process', 'In Process'), ('Delivered', 'Delivered'), ('Not Delivered', 'Not Delivered')], default='In Process', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
    ]
