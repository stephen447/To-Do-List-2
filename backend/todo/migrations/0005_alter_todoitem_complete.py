# Generated by Django 4.2.2 on 2023-06-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todoitem_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
