# Generated by Django 4.2 on 2023-04-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_delete_doctor_delete_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.IntegerField(default=1),
        ),
    ]
