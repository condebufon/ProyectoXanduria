# Generated by Django 5.1.3 on 2024-11-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pais',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]