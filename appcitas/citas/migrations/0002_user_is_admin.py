# Generated by Django 4.2.5 on 2023-10-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("citas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
