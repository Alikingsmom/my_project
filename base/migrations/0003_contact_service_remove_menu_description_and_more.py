# Generated by Django 4.2.2 on 2023-07-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_our_services"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="menu",
            name="description",
        ),
        migrations.DeleteModel(
            name="Our_Services",
        ),
        migrations.AddField(
            model_name="service",
            name="menu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="base.menu"
            ),
        ),
    ]
