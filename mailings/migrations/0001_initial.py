# Generated by Django 5.0.3 on 2024-06-27 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="почта"
                    ),
                ),
                ("fio", models.CharField(max_length=150, verbose_name="ФИО")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="комментарий"),
                ),
            ],
            options={
                "verbose_name": "клиент",
                "verbose_name_plural": "клиенты",
            },
        ),
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attempt_time",
                    models.DateTimeField(verbose_name="дата и время последней попытки"),
                ),
                ("attempt", models.BooleanField(verbose_name="статус попытки")),
                (
                    "response",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="ответ почтового сервера",
                    ),
                ),
            ],
            options={
                "verbose_name": "лог попыток отправки письма",
                "verbose_name_plural": "логи попыток отправки писем",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(max_length=50, verbose_name="тема письма"),
                ),
                ("body", models.TextField(verbose_name="тело письма")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_time",
                    models.DateTimeField(verbose_name="время начала отправки рассылки"),
                ),
                (
                    "end_time",
                    models.DateTimeField(
                        verbose_name="время окончания отправки рассылки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("раз в день", "раз в день"),
                            ("раз в неделю", "раз в неделю"),
                            ("раз в месяц", "раз в месяц"),
                        ],
                        max_length=20,
                        verbose_name="периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("завершена", "завершена"),
                            ("создана", "создана"),
                            ("запущена", "запущена"),
                        ],
                        default="создана",
                        max_length=20,
                        verbose_name="статус рассылки",
                    ),
                ),
                (
                    "client",
                    models.ManyToManyField(to="mailings.client", verbose_name="клиент"),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailings.message",
                        verbose_name="сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
    ]
