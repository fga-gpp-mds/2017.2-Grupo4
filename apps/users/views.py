# Arquivo: /apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from datetime import date
from apps.risk_rating.ml_classifier import MachineLearning
from apps.risk_rating.ml_classifier_range2 import MachineLearningRange2
from apps.users.forms import RegistrationStaffForm
from apps.users.forms import RegistrationPatientForm
from apps.users.forms import EditPatientForm
from .models import Patient, Staff

ml = MachineLearning()
ml2 = MachineLearningRange2()


def landing_page(request):

    return render(request, 'landing_page/landingPage.html', {})


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/home")
        else:

            kwargs['extra_context'] = {'next': reverse('users:login'),
                                       'errors': 'Usuário e/ou senha inválido.'
                                       }

            kwargs['template_name'] = 'users/user_login/login.html'
            return login(request, *args, **kwargs)

    kwargs['extra_context'] = {'next': reverse('users:login')}
    kwargs['template_name'] = 'users/user_login/login.html'
    return login(request, *args, **kwargs)


@login_required(redirect_field_name='', login_url='users:login')
def home(request):
    """
    triggers the machine learning based on patient's age range
    """
    patients = Patient.objects.all()
    patient = None
    classification = None
    form = None
    if request.method == "POST":
            form = request.POST
            subject_patient_id = form.get("patient_id")
            subject_patient = Patient.objects.get(id=subject_patient_id)

            # machine learning methods are called here:
            if subject_patient.age_range == 1:
                patient = get_under_28_symptoms(form)
                probability = ml.calc_probabilities(patient)
                classification = ml.classify_patient(patient)
                impact_list = ml.feature_importance()
            elif subject_patient.age_range == 2:
                patient = get_29d_2m_symptoms(form)
                probability = ml2.calc_probabilities(patient)
                classification = ml2.classify_patient(patient)
                impact_list = ml2.feature_importance()
            # to add another age range, use another elif
            else:
                pass

            define_patient_classification(subject_patient, classification)

            # printing the results:
            print(probability)
            print(classification)
            print(impact_list)

    return render(request, 'users/user_home/main_home.html',
                           {'patients': patients,
                            'classification': classification})


def define_patient_classification(subject_patient, classification):
    """
    edit patient's classification attribute
    """
    if classification == 'AtendimentoImediato':
        subject_patient.classification = 1
    elif classification == 'AmbulatorialGeral':
        subject_patient.classification = 2
    elif classification == 'AtendimentoHospitalar':
        subject_patient.classification = 3
    else:
        pass

    subject_patient.save()


def check_patient_problem(problem):
    if problem is not None:
        problem = 1
    else:
        problem = 0

    return problem


def logout_view(request, *args, **kwargs):
    """
    Define the logout page
    """
    kwargs['next_page'] = reverse('users:landing_page')
    return logout(request, *args, **kwargs)


def sign_up_profile(request):
    form = RegistrationStaffForm()
    if request.method == 'POST':
        form = RegistrationStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    return render(request, 'users/user_login/registerUser.html',
                  {'form': form})


def specify_age_range(age_range, aux_age_range, form):
    if age_range >= 0 and age_range <= 28:
        aux_age_range = form.cleaned_data['age_range'] = 1
    elif age_range > 28 and age_range <= 90:
        aux_age_range = form.cleaned_data['age_range'] = 2
    elif age_range > 90 and age_range <= 730:
        aux_age_range = form.cleaned_data['age_range'] = 3
    elif age_range > 730 and age_range <= 3650:
        aux_age_range = form.cleaned_data['age_range'] = 4
    elif age_range > 3650:
        aux_age_range = form.cleaned_data['age_range'] = 5
    else:
        aux_age_range = form.cleaned_data['age_range'] = 0
    instance = form.save(commit=False)
    instance.age_range = aux_age_range
    instance.save()


def calculate_age_range(form):
    birth_date = form.cleaned_data['birth_date']
    age_range = (date.today() - birth_date).days
    int(age_range)
    aux_age_range = 0
    specify_age_range(age_range, aux_age_range, form)


@login_required(redirect_field_name='', login_url='users:login')
def register_patient(request):
    form = RegistrationPatientForm()
    if request.method == 'POST':
        form = RegistrationPatientForm(request.POST)
        if form.is_valid():
            if ['birth_date'] in form.changed_data:
                calculate_age_range(form)
            else:
                pass    
            form.save()
            return redirect('users:home')

    return render(request, 'users/user_home/registerPatient.html',
                  {'form': form})


@login_required(redirect_field_name='', login_url='users:login')
def queue_patient(request, cpf_patient):
    patients = Patient.objects.filter(cpf=cpf_patient)
    patient = Patient.objects.get(cpf=cpf_patient)
    patientsInQueue = Patient.objects.all()
    patientList = list()
    for patient0 in patientsInQueue:
        patientList.append(patient0.patient)
    if patient in patientList:
        return render(request, 'users/queuePatient.html',
                               {'patientList': patientList})
    else:
        queuedPatient = Patient.objects.create(patient=patient)
        queuedPatient.save()
        patientList.append(patient)
        return render(request, 'users/queuePatient.html',
                               {'patients': patients})
    return render(request, 'users/queuePatient.html', {'patients': patients})


@login_required(redirect_field_name='', login_url='users:login')
def manage_accounts_view(request):
    staffs = Staff.objects.all()
    return render(request, 'users/manageAccounts.html', {'staffs': staffs})


@login_required(redirect_field_name='', login_url='users:login')
def edit_accounts_view(request, id_user):
    staff = Staff.objects.filter(id_user=id_user)
    if len(staff) == 1:
        return render(request, 'users/editAccounts.html', {'staff': staff[0]})
    return render(request, 'users/editAccounts.html', status=404)


@login_required(redirect_field_name='', login_url='users:login')
def staff_remove(request, id_user):
    staff = Staff.objects.filter(id_user=id_user)
    staff.delete()
    return HttpResponseRedirect(reverse('users:manage_accounts'))


@login_required(redirect_field_name='', login_url='users:login')
def patient_remove(request, id):
    patient = Patient.objects.filter(id=id)
    patient.delete()
    return HttpResponseRedirect(reverse('users:home'))


@login_required(redirect_field_name='', login_url='users:login')
def edit_patient(request, id):
    """
    edit an existing patient with post method
    """
    patient = Patient.objects.filter(id=id)[0]
    form = EditPatientForm()

    status = 200

    if request.method == 'POST':
        form = EditPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('users:home')
        else:
            status = 400
    return render(request, 'users/editPatient.html',
                  {'patient': patient, 'form': form}, status=status)


@login_required(redirect_field_name='', login_url='users:login')
def show_patient_view(request, cpf):
    """
    return rendered text from showPatient
    """
    patient = Patient.objects.filter(cpf=cpf)
    if len(patient) == 1:
        return render(request, 'users/showPatient.html', {'patient': patient})
    return render(request, 'users/showPatient.html', status=404)


def get_under_28_symptoms(form):
    """
    get symptoms from form to build patient's clinical condition
    """
    dispineia = check_patient_problem(form.get("dispineia"))
    ictericia = check_patient_problem(form.get("ictericia"))
    consciencia = check_patient_problem(form.get("consciência"))
    cianose = check_patient_problem(form.get("cianose"))
    febre = check_patient_problem(form.get("febre"))
    solucos = check_patient_problem(form.get("solucos"))
    prostracao = check_patient_problem(form.get("prostracao"))
    vomitos = check_patient_problem(form.get("vomitos"))
    tosse = check_patient_problem(form.get("tosse"))
    coriza = check_patient_problem(form.get("coriza"))
    obstrucaoNasal = check_patient_problem(form.get("obstrucaoNasal"))
    convulsaoMomento = check_patient_problem(form.get("convulsaoMomento"))
    diarreia = check_patient_problem(form.get("diarreia"))
    choroIncosolavel = check_patient_problem(form.get("choroIncosolavel"))
    dificuldadeEvacuar = check_patient_problem(form.get("dificuldadeEvacuar"))
    naoSugaSeio = check_patient_problem(form.get("naoSugaSeio"))
    manchaPele = check_patient_problem(form.get("manchaPele"))
    salivacao = check_patient_problem(form.get("salivacao"))
    queda = check_patient_problem(form.get("queda"))
    chiadoPeito = check_patient_problem(form.get("chiadoPeito"))
    diminuicaoDiurese = check_patient_problem(form.get("diminuicaoDiurese"))
    dorAbdominal = check_patient_problem(form.get("dorAbdominal"))
    dorOuvido = check_patient_problem(form.get("dorOuvido"))
    fontanelaAbaulada = check_patient_problem(form.get("fontanelaAbaulada"))
    secrecaoUmbigo = check_patient_problem(form.get("secrecaoUmbigo"))
    secrecaoOcular = check_patient_problem(form.get("secrecaoOcular"))
    sangueFezes = check_patient_problem(form.get("sangueFezes"))
    convulsaoHoje = check_patient_problem(form.get("convulsaoHoje"))

    patient = [[
        dispineia,
        ictericia,
        consciencia,
        cianose,
        febre,
        solucos,
        prostracao,
        vomitos,
        tosse,
        coriza,
        obstrucaoNasal,
        convulsaoMomento,
        diarreia,
        choroIncosolavel,
        dificuldadeEvacuar,
        naoSugaSeio,
        manchaPele,
        salivacao,
        queda,
        chiadoPeito,
        diminuicaoDiurese,
        dorAbdominal,
        dorOuvido,
        fontanelaAbaulada,
        secrecaoUmbigo,
        secrecaoOcular,
        sangueFezes,
        convulsaoHoje,
    ]]

    return patient


def get_29d_2m_symptoms(form):
    """
    get symptoms from form to build patient's clinical condition
    """
    dispineia = check_patient_problem(form.get("dispineia"))
    ictericia = check_patient_problem(form.get("ictericia"))
    consciencia = check_patient_problem(form.get("consciência"))
    cianose = check_patient_problem(form.get("cianose"))
    febre = check_patient_problem(form.get("febre"))
    solucos = check_patient_problem(form.get("solucos"))
    prostracao = check_patient_problem(form.get("prostracao"))
    vomitos = check_patient_problem(form.get("vomitos"))
    tosse = check_patient_problem(form.get("tosse"))
    coriza = check_patient_problem(form.get("coriza"))
    obstrucaoNasal = check_patient_problem(form.get("obstrucaoNasal"))
    convulsaoMomento = check_patient_problem(form.get("convulsaoMomento"))
    diarreia = check_patient_problem(form.get("diarreia"))
    dificuldadeEvacuar = check_patient_problem(form.get("dificuldadeEvacuar"))
    naoSugaSeio = check_patient_problem(form.get("naoSugaSeio"))
    manchaPele = check_patient_problem(form.get("manchaPele"))
    salivacao = check_patient_problem(form.get("salivacao"))
    queda = check_patient_problem(form.get("queda"))
    chiadoPeito = check_patient_problem(form.get("chiadoPeito"))
    diminuicaoDiurese = check_patient_problem(form.get("diminuicaoDiurese"))
    dorAbdominal = check_patient_problem(form.get("dorAbdominal"))
    dorOuvido = check_patient_problem(form.get("dorOuvido"))
    fontanelaAbaulada = check_patient_problem(form.get("fontanelaAbaulada"))
    secrecaoUmbigo = check_patient_problem(form.get("secrecaoUmbigo"))
    secrecaoOcular = check_patient_problem(form.get("secrecaoOcular"))
    sangueFezes = check_patient_problem(form.get("sangueFezes"))
    convulsaoHoje = check_patient_problem(form.get("convulsaoHoje"))

    patient = [[
        dispineia,
        ictericia,
        consciencia,
        cianose,
        febre,
        solucos,
        prostracao,
        vomitos,
        tosse,
        coriza,
        obstrucaoNasal,
        convulsaoMomento,
        diarreia,
        dificuldadeEvacuar,
        naoSugaSeio,
        manchaPele,
        salivacao,
        queda,
        chiadoPeito,
        diminuicaoDiurese,
        dorAbdominal,
        dorOuvido,
        fontanelaAbaulada,
        secrecaoUmbigo,
        secrecaoOcular,
        sangueFezes,
        convulsaoHoje,
    ]]

    return patient
