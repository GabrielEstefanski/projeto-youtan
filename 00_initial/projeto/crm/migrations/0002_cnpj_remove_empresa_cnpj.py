# Generated by Django 4.1.5 on 2023-01-16 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnpj',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='crm.empresa')),
                ('cnpj', models.CharField(max_length=50, verbose_name='CNPJ')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
            ],
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='cnpj',
        ),
    ]
