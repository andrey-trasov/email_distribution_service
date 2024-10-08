# Generated by Django 4.2.9 on 2024-07-31 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0003_alter_newsletter_periodicity_alter_newsletter_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="logs",
            name="comments",
            field=models.TextField(
                blank=True, max_length=50, null=True, verbose_name="Комментарии"
            ),
        ),
        migrations.AddField(
            model_name="logs",
            name="mailing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attempts",
                to="mailings.newsletter",
            ),
        ),
        migrations.AddField(
            model_name="logs",
            name="name",
            field=models.CharField(
                default="Рассылка", max_length=50, verbose_name="Название рассылки"
            ),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Название рассылки"
            ),
        ),
    ]
