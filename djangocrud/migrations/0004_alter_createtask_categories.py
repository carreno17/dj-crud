# Generated by Django 3.2.15 on 2022-12-21 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocrud', '0003_alter_createtask_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtask',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangocrud.categories'),
        ),
    ]
