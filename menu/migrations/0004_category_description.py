# Generated by Django 5.1.3 on 2024-11-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_category_alter_menuitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
