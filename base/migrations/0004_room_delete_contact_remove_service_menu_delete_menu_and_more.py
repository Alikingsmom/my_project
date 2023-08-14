# Generated by Django 4.2.2 on 2023-07-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_contact_service_remove_menu_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("updated", models.DateTimeField(auto_now=True)),
                ("crated", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.RemoveField(
            model_name="service",
            name="menu",
        ),
        migrations.DeleteModel(
            name="Menu",
        ),
        migrations.DeleteModel(
            name="Service",
        ),
    ]