# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 20:0379efd95b706e7691
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalState_28d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, max_length=150, verbose_name='ID do Paciente')),
                ('dispineia', models.BooleanField(default=False, verbose_name='Dispinéia')),
                ('ictericia', models.BooleanField(default=False, verbose_name='Icterícia')),
                ('perdada_consciencia', models.BooleanField(default=False, verbose_name='Perda de Consciência')),
                ('cianose', models.BooleanField(default=False, verbose_name='Cianose')),
                ('febre', models.BooleanField(default=False, verbose_name='Febre')),
                ('solucos', models.BooleanField(default=False, verbose_name='Soluços')),
                ('prostracao', models.BooleanField(default=False, verbose_name='Prostração')),
                ('vomitos', models.BooleanField(default=False, verbose_name='Vômitos')),
                ('tosse', models.BooleanField(default=False, verbose_name='Tosse')),
                ('coriza', models.BooleanField(default=False, verbose_name='Coriza')),
                ('obstrucao_nasal', models.BooleanField(default=False, verbose_name='Obstrução Nasal')),
                ('convulcao_no_momento', models.BooleanField(default=False, verbose_name='Convulção no momento')),
                ('diarreia', models.BooleanField(default=False, verbose_name='Diarréia')),
                ('choro_inconsolavel', models.BooleanField(default=False, verbose_name='Choro Inconsolável')),
                ('dificuldade_evacuar', models.BooleanField(default=False, verbose_name='Dificuldade de Evacuar')),
                ('nao_suga_seio', models.BooleanField(default=False, verbose_name='Não suga o seio')),
                ('manchas_na_pele', models.BooleanField(default=False, verbose_name='Manchas na pele')),
                ('salivacao', models.BooleanField(default=False, verbose_name='Salivação')),
                ('queda', models.BooleanField(default=False, verbose_name='Queda')),
                ('chiado_no_peito', models.BooleanField(default=False, verbose_name='Chiado no peito')),
                ('diminuicao_da_diurese', models.BooleanField(default=False, verbose_name='Diminuição da Diurese')),
                ('dor_abdominal', models.BooleanField(default=False, verbose_name='Dor abdominal')),
                ('dor_de_ouvido', models.BooleanField(default=False, verbose_name='Dor de ouvido')),
                ('fontanela_abaulada', models.BooleanField(default=False, verbose_name='Fontanela abaulada')),
                ('secrecao_no_umbigo', models.BooleanField(default=False, verbose_name='Secreção no umbigo')),
                ('secrecao_ocular', models.BooleanField(default=False, verbose_name='Secreção ocular')),
                ('sangue_nas_fezes', models.BooleanField(default=False, verbose_name='Sangue nas fezes')),
                ('convulsao_hoje', models.BooleanField(default=False, verbose_name='Relato de convulsão hoje')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalState_29d_2m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, max_length=150, verbose_name='ID do Paciente')),
                ('dispineia', models.BooleanField(default=False, verbose_name='Dispinéia')),
                ('ictericia', models.BooleanField(default=False, verbose_name='Icterícia')),
                ('perdada_consciencia', models.BooleanField(default=False, verbose_name='Perda de Consciência')),
                ('cianose', models.BooleanField(default=False, verbose_name='Cianose')),
                ('febre', models.BooleanField(default=False, verbose_name='Febre')),
                ('solucos', models.BooleanField(default=False, verbose_name='Soluços')),
                ('prostracao', models.BooleanField(default=False, verbose_name='Prostração')),
                ('vomitos', models.BooleanField(default=False, verbose_name='Vômitos')),
                ('tosse', models.BooleanField(default=False, verbose_name='Tosse')),
                ('coriza', models.BooleanField(default=False, verbose_name='Coriza')),
                ('obstrucao_nasal', models.BooleanField(default=False, verbose_name='Obstrução Nasal')),
                ('convulcao_no_momento', models.BooleanField(default=False, verbose_name='Convulção no momento')),
                ('diarreia', models.BooleanField(default=False, verbose_name='Diarréia')),
                ('dificuldade_evacuar', models.BooleanField(default=False, verbose_name='Dificuldade de Evacuar')),
                ('nao_suga_seio', models.BooleanField(default=False, verbose_name='Não suga o seio')),
                ('manchas_na_pele', models.BooleanField(default=False, verbose_name='Manchas na pele')),
                ('salivacao', models.BooleanField(default=False, verbose_name='Salivação')),
                ('queda', models.BooleanField(default=False, verbose_name='Queda')),
                ('chiado_no_peito', models.BooleanField(default=False, verbose_name='Chiado no peito')),
                ('diminuicao_da_diurese', models.BooleanField(default=False, verbose_name='Diminuição da Diurese')),
                ('dor_abdominal', models.BooleanField(default=False, verbose_name='Dor abdominal')),
                ('dor_de_ouvido', models.BooleanField(default=False, verbose_name='Dor de ouvido')),
                ('fontanela_abaulada', models.BooleanField(default=False, verbose_name='Fontanela abaulada')),
                ('secrecao_no_umbigo', models.BooleanField(default=False, verbose_name='Secreção no umbigo')),
                ('secrecao_ocular', models.BooleanField(default=False, verbose_name='Secreção ocular')),
                ('sangue_nas_fezes', models.BooleanField(default=False, verbose_name='Sangue nas fezes')),
                ('convulsao_hoje', models.BooleanField(default=False, verbose_name='Relato de convulsão hoje')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalState_2m_3y',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, max_length=150, verbose_name='ID do Paciente')),
                ('dispineia', models.BooleanField(default=False, verbose_name='Dispinéia')),
                ('ictericia', models.BooleanField(default=False, verbose_name='Icterícia')),
                ('perdada_consciencia', models.BooleanField(default=False, verbose_name='Perda de Consciência')),
                ('cianose', models.BooleanField(default=False, verbose_name='Cianose')),
                ('febre', models.BooleanField(default=False, verbose_name='Febre')),
                ('solucos', models.BooleanField(default=False, verbose_name='Soluços')),
                ('prostracao', models.BooleanField(default=False, verbose_name='Prostração')),
                ('vomitos', models.BooleanField(default=False, verbose_name='Vômitos')),
                ('tosse', models.BooleanField(default=False, verbose_name='Tosse')),
                ('coriza', models.BooleanField(default=False, verbose_name='Coriza')),
                ('obstrucao_nasal', models.BooleanField(default=False, verbose_name='Obstrução Nasal')),
                ('convulcao_no_momento', models.BooleanField(default=False, verbose_name='Convulção no momento')),
                ('diarreia', models.BooleanField(default=False, verbose_name='Diarréia')),
                ('dificuldade_evacuar', models.BooleanField(default=False, verbose_name='Dificuldade de Evacuar')),
                ('nao_suga_seio', models.BooleanField(default=False, verbose_name='Não suga o seio')),
                ('manchas_na_pele', models.BooleanField(default=False, verbose_name='Manchas na pele')),
                ('salivacao', models.BooleanField(default=False, verbose_name='Salivação')),
                ('queda', models.BooleanField(default=False, verbose_name='Queda')),
                ('chiado_no_peito', models.BooleanField(default=False, verbose_name='Chiado no peito')),
                ('diminuicao_da_diurese', models.BooleanField(default=False, verbose_name='Diminuição da Diurese')),
                ('dor_abdominal', models.BooleanField(default=False, verbose_name='Dor abdominal')),
                ('dor_de_ouvido', models.BooleanField(default=False, verbose_name='Dor de ouvido')),
                ('fontanela_abaulada', models.BooleanField(default=False, verbose_name='Fontanela abaulada')),
                ('secrecao_no_umbigo', models.BooleanField(default=False, verbose_name='Secreção no umbigo')),
                ('secrecao_ocular', models.BooleanField(default=False, verbose_name='Secreção ocular')),
            ],
        ),
    ]
