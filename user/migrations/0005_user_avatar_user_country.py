# Generated by Django 4.2.9 on 2024-08-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите свой аватар",
                null=True,
                upload_to="users/avatars/",
                verbose_name="Аватар",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                blank=True,
                help_text="Введите свою страну проживания",
                max_length=50,
                null=True,
                verbose_name="Страна",
            ),
        ),
    ]
