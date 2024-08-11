# Generated by Django 3.1.4 on 2024-08-06 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_remove_lead_organizations'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organizations',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
    ]