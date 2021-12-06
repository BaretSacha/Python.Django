# Generated by Django 3.0.8 on 2020-11-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20201107_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
            ],
        ),
    ]
