# Arquivo: apps/risk_rating/forms.py
from django import forms
from apps.risk_rating.models import ClinicalState_28d
from apps.risk_rating.models import ClinicalState_29d_2m
from apps.risk_rating.models import ClinicalState_2m_3y
from apps.risk_rating.models import ClinicalState_10yMore


class ClinicalState_28dForm(forms.ModelForm):
    """
    Defining fields for under 28 days patient's clinical state
    """
    class Meta:
        model = ClinicalState_28d
        fields = ['patient_id1', 'dispineia', 'ictericia',
                  'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse',
                  'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'choro_inconsolavel', 'dificuldade_evacuar',
                  'nao_suga_seio', 'manchas_na_pele', 'salivacao',
                  'chiado_no_peito', 'diminuicao_da_diurese', 'dor_abdominal',
                  'fontanela_abaulada', 'secrecao_no_umbigo',
                  'secrecao_ocular', 'sangue_nas_fezes', 'convulsao_hoje']


class ClinicalState_29d_2mForm(forms.ModelForm):
    """
    Defining fields patients (29 days and 2 months old) clinical state
    """
    class Meta:
        model = ClinicalState_29d_2m
        fields = ['patient_id2', 'dispineia', 'ictericia',
                  'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse',
                  'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'dificuldade_evacuar', 'nao_suga_seio',
                  'manchas_na_pele', 'salivacao', 'chiado_no_peito',
                  'diminuicao_da_diurese', 'dor_abdominal',
                  'fontanela_abaulada', 'secrecao_no_umbigo',
                  'secrecao_ocular', 'sangue_nas_fezes', 'convulsao_hoje']


class ClinicalState_2m_3yForm(forms.ModelForm):
    """
    Defining fields patients (29 days and 2 months old) clinical state
    """
    class Meta:
        model = ClinicalState_2m_3y
        fields = ['patient_id3', 'dispineia', 'ictericia',
                  'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse',
                  'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'dificuldade_evacuar', 'nao_suga_seio',
                  'manchas_na_pele', 'salivacao', 'chiado_no_peito',
                  'diminuicao_da_diurese', 'dor_abdominal',
                  'fontanela_abaulada', 'secrecao_no_umbigo',
                  'secrecao_ocular']


class ClinicalState_10yMoreForm(forms.ModelForm):
    """
    Defining fields patients (29 days and 2 months old) clinical state
    """
    class Meta:
        model = ClinicalState_10yMore
        fields = ['patient_id5', 'mais_de_72h_febre', 'menos_de_72h_febre',
                  'tontura', 'corpo_estranho', 'dor_de_dente', 'disuria',
                  'urina_concentrada', 'dispineia', 'dor_toracica',
                  'choque_eletrico', 'quase_afogamento', 'artralgia',
                  'ictericia', 'perda_da_consciencia', 'palidez', 'cianose',
                  'solucos', 'prostracao', 'febre', 'vomitos', 'tosse',
                  'coriza', 'espirros', 'hiperemia_conjuntival',
                  'secrecao_ocular', 'obstrucao_nasal', 'convulsao',
                  'diarreia', 'dificuldade_evacuar', 'cefaleia',
                  'manchas_na_pele', 'salivacao', 'queda', 'hiporexia',
                  'salivacao', 'hiporexia', 'constipacao', 'chiado_no_peito',
                  'diminuicao_da_diurese', 'dor_abdominal', 'otalgia',
                  'epistaxe', 'otorreia', 'edema', 'adenomegalias',
                  'dor_articular', 'dificuldade_de_marcha', 'sonolencia',
                  'secrecao_ocular', 'dor_muscular', 'dor_retroorbitaria']