# Generated by Django 4.1.2 on 2022-10-28 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='token',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]