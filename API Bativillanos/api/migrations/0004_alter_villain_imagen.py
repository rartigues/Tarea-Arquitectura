# Generated by Django 4.2.3 on 2023-07-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_usuario_power_villano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villain',
            name='imagen',
            field=models.TextField(),
        ),
    ]
