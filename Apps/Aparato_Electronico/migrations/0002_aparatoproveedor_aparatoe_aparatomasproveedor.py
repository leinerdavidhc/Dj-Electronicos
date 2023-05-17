# Generated by Django 4.2.1 on 2023-05-17 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedor', '0001_initial'),
        ('Aparato_Electronico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AparatoProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aparatoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aparato_Electronico.aparatoe')),
                ('proveedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedores')),
            ],
        ),
        migrations.AddField(
            model_name='aparatoe',
            name='aparatomasProveedor',
            field=models.ManyToManyField(through='Aparato_Electronico.AparatoProveedor', to='Proveedor.proveedores', verbose_name='AparatoProveedor'),
        ),
    ]
