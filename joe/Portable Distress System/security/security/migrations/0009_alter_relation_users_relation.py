# Generated by Django 4.1.5 on 2023-02-10 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0008_relation_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation_users',
            name='relation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='security.contact_info', to_field='roll'),
        ),
    ]
