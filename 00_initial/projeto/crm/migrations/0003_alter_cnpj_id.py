# Generated by Django 4.1.5 on 2023-02-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_cnpj_remove_empresa_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnpj',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
