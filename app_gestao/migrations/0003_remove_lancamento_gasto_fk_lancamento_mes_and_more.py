# Generated by Django 4.0.2 on 2022-04-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestao', '0002_alter_banco_criado_em_alter_categoria_criado_em_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamento',
            name='mes',
            field=models.CharField(choices=[('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Março'), ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'), ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')], default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banco',
            name='fechamento_fatura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='banco',
            name='vencimento_fatura',
            field=models.IntegerField(),
        ),
    ]
