# Generated by Django 4.0.2 on 2022-04-20 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestao', '0005_gasto_lancamento_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='fechamento_fatura',
            field=models.CharField(max_length=2, verbose_name='Fechamento da fatura'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='usuario_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestao.usuario', verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='vencimento_fatura',
            field=models.CharField(max_length=2, verbose_name='Vencimento da fatura'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='cor',
            field=models.CharField(blank=True, default='#B60691', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, max_length=28, null=True),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='banco_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestao.banco', verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='mes',
            field=models.CharField(choices=[('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Março'), ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'), ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')], max_length=2, verbose_name='Mês'),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='usuario_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestao.usuario', verbose_name='Usuário'),
        ),
    ]
