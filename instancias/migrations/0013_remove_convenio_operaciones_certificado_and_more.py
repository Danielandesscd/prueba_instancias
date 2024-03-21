# Generated by Django 5.0.2 on 2024-03-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instancias', '0012_formatoentrega_operacioncertificado_operacionfirmado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convenio',
            name='operaciones_certificado',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='operaciones_firmado',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='operaciones_otp',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='tipos_certificado',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='vigencias_certificado',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='certificados_seleccionados',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='formatos_entrega',
        ),
        migrations.AddField(
            model_name='convenio',
            name='formatos_entrega_permi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convenio',
            name='o_cert_permi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convenio',
            name='o_firmado_permi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convenio',
            name='o_otp_permi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convenio',
            name='vigencias_permi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OperacionCertificado',
        ),
        migrations.DeleteModel(
            name='OperacionFirmado',
        ),
        migrations.DeleteModel(
            name='OperacionOTP',
        ),
        migrations.DeleteModel(
            name='TipoCertificado',
        ),
        migrations.DeleteModel(
            name='VigenciaCertificado',
        ),
    ]