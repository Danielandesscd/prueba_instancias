# Generated by Django 4.2.5 on 2024-03-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instancias', '0007_merge_20240311_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='convenio',
            name='certificados_seleccionados',
            field=models.ManyToManyField(related_name='convenios', to='instancias.certificado'),
        ),
    ]