# Generated by Django 3.2.5 on 2021-08-29 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_categories_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
