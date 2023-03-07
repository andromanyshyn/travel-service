# Generated by Django 4.1.7 on 2023-03-07 10:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('service_function', '0004_alter_transport_code_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='code_name',
            field=models.UUIDField(default=uuid.UUID('30adb3c4-4040-494b-90c0-be09946d694a'), unique=True),
        ),
        migrations.AlterField(
            model_name='waybills',
            name='list_of_transport',
            field=models.ManyToManyField(related_name='transports', to='service_function.transport'),
        ),
    ]
