# Generated by Django 4.1.4 on 2022-12-29 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contactus_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='home/sliders')),
                ('Link', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Block_Buster_Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
