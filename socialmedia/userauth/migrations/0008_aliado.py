# Generated by Django 5.0.2 on 2024-05-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_followers_delete_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('correo_empresa', models.EmailField(max_length=254)),
                ('oferta', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('telefono_empresa', models.CharField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='aliados/')),
            ],
        ),
    ]
