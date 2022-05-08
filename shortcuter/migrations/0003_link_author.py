# Generated by Django 4.0 on 2022-05-08 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('shortcuter', '0002_rename_slug_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]