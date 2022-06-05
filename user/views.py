from django.shortcuts import render
import random
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from medbro.models import Notification
from .models import User, Hospitals, Occupation, Xamshira, Post_maqolas, Post_tabletkas, Kassallik
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from .forms import AddMaqolaForm, ChangeMaqolaForm
from django_quill.fields import QuillField

# Create your views here.
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        random_code = random.randrange(1001, 9999)
        print(random_code)
        import smtplib
        sender_address = 'yuldashevjavohir15@gmail.com'
        sender_pass = 'jlkl hctl glyj jjlu'
        receiver_address = str(email)
        gmail_user = sender_address
        gmail_password = sender_pass
        sent_from = gmail_user
        to = [receiver_address]
        subject = 'importtant code '
        body = f'Hey, what {random_code}'
        email_text = f"""\
            From: {gmail_user}
            To: {to[0]}
            Subject: {subject}
            Body: {body}
            """
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, body)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')
        username = request.POST['username']
        password = request.POST['password']


        return render(request, 'input_code.html', {
            'email':email,
            'username':username,
            'password':password,
            'random':random_code,
        })

    else:
        return render(request, 'singup.html', {})

def check_code(request):
    input_code = request.POST['input_code']
    random_code = request.POST['random']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    if str(input_code) == str(random_code):
        auth,get = User.objects.get_or_create(email=email, password=password, full_name=username)
        auth = authenticate(request, email=email, password=password, full_name=username)
        auth = User.objects.get(email=email, password=password, full_name=username)
        login(request, auth)
        return redirect('login.html')
    else:
        return redirect('input_code.html')

def add_nurse(request):
    all_shifoxona = Hospitals.objects.all()
    all_occupations = Occupation.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        random_code = random.randrange(1001, 9999)
        print(random_code)
        import smtplib
        sender_address = 'yuldashevjavohir15@gmail.com'
        sender_pass = 'jlkl hctl glyj jjlu'
        receiver_address = str(email)
        gmail_user = sender_address
        gmail_password = sender_pass
        sent_from = gmail_user
        to = [receiver_address]
        subject = 'importtant code '
        body = f'Hey, what {random_code}'
        email_text = f"""\
            From: {gmail_user}
            To: {to[0]}
            Subject: {subject}
            Body: {body}
            """
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, body)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        passport = request.POST['passport']

        medicine = request.POST['medicine']
        shifoxona = medicine
        minut_10 = request.POST['10_minut']
        minut_20 = request.POST['20_minut']
        occupation = request.POST['occupation']


        return render(request, 'nurse_input_code.html', {
            'email':email,
            'full_name':full_name,
            'password':password,
            'random':random_code,
            'passport':passport,
            'shifoxona': shifoxona,
            'minut_10': minut_10,
            'minut_20': minut_20,
            'occupation': occupation,
            'all_shifoxona': all_shifoxona,
            'all_occupations': all_occupations,

        })

    else:
        return render(request, 'signup_nurse.html', {

            'all_shifoxona': all_shifoxona,
            'all_occupations': all_occupations,})

def check_code_hamshira(request):
    input_code = request.POST['input_code']
    random_code = request.POST['random']
    email = request.POST['email']
    full_name = request.POST['full_name']
    password = request.POST['password']
    shifoxona = request.POST['shifoxona']
    minut_10 = request.POST['minut_10']
    minut_20 = request.POST['minut_20']
    occupation = request.POST['occupation']

    if str(input_code) == str(random_code):
        auth,get = User.objects.get_or_create(
            email=email, password=password, full_name=full_name,credit_card='12345678910111411')
        xamshira1,get = Xamshira.objects.get_or_create(
            shifoxona_id=shifoxona,
            minut_10=minut_10, minut_20=minut_20, kasb_id=occupation
        )
        medicine = Hospitals.objects.get(id=shifoxona)
        medicine = medicine.main_nurse
        xamshira1.user = (auth)
        xamshira1.save()
        Notification.objects.create(
            text=f'@{full_name} Sizning shifoxonangizga xamshira bo`lib ishga kirdi',
            xamshira=xamshira1,
            to_user=medicine.user)
        auth = authenticate(request, email=email, password=password, full_name=full_name)
        auth = User.objects.get(email=email, password=password, full_name=full_name)
        login(request, auth)
        return redirect('login.html')
    else:
        return redirect('nurse_input_code.html')

def all_posts_view(request):
    try:
        all_maqola = Post_maqolas.objects.all()[:6]
    except:
        all_maqola = Post_maqolas.objects.all()

    all_tabletka = Post_tabletkas.objects.all()
    return render(request, 'MedBrat-project\index.html', {'maqolas': all_maqola})

def maqola_view(request, pk):
    maqola = Post_maqolas.objects.get(pk=pk)
    return render(request, 'post/maqola_detail.html', {'maqola': maqola})

def tabletka_view(request, pk):
    tabletka = Post_tabletkas.objects.get(pk=pk)
    return render(request, 'post/tabletka_detail.html', {'tabletka':tabletka})

def add_maqola(request):
   return render(request, 'post/add_maqola.html', {'form':AddMaqolaForm()})

def add_add_maqola(request):
    xamshira = Xamshira.objects.get(user=request.user)
    content = request.POST['content']
    name = request.POST['name']
    post = Post_maqolas.objects.create(
        quil=content,
        author=xamshira,
        name=name
    )
    post.save()
    return redirect('all_maqola')

# class ChangeMaqola(UpdateView):
#     model = Post_maqolas
#     fields = [ 'name', 'quil']
#     template_name = 'post/change_maqola.html'
def change_maqola(request, pk):
    post = Post_maqolas.objects.get(pk=pk)
    return render(request, 'post/change_maqola.html', {'form': ChangeMaqolaForm(instance=post), 'post':post, 'pk':pk})

def change_change_maqola(request, pk):
    post = Post_maqolas.objects.get(pk=pk)
    post.name = request.POST['name']
    post.quil = request.POST['quil']

    post.save()
    return redirect('all_maqola')

class DeleteMaqolaView(DeleteView):
    model = Post_maqolas
    success_url = reverse_lazy('all_maqola')
    template_name = 'post/delete_maqola.html'


def search(request):
    search_words = request.POST['searched']
    hamshira = Xamshira.objects.filter(paid=True)
    post_hamshira = Post_maqolas.objects.filter(author__in=hamshira)
    searched_paid_post = post_hamshira.filter(name__icontains=search_words)
    searched_paid_post2 = post_hamshira.filter(quil__icontains=search_words)
    maqola = Post_maqolas.objects.filter(name__icontains=search_words)
    maqola2 = Post_maqolas.objects.filter(quil__icontains=search_words)
    dori = Post_tabletkas.objects.filter(name__icontains=search_words)
    kasalik = Kassallik.objects.filter(name__icontains=search_words)
    dori2 = Post_tabletkas.objects.filter(kasalik__in=kasalik)
    dori3 = Post_tabletkas.objects.filter(quil__icontains=search_words)
    list1 = []
    list2 = []

    for i in searched_paid_post:
        list1.insert(0, i)
    for i in searched_paid_post2:
        if i not in list1:
            list1.insert(0, i)
    for i in maqola:
        if i not in list1:
            list1.append(i)

    for i in maqola2:
        if i not in list1:
            list1.append(i)
    for i in dori:
        list2.append(i)
    for i in dori2:
        if i not in list2:
            list2.append(i)
    for i in dori3:
        if i not in list2:
            list2.append(i)
    length1 = len(list1)
    length2 = len(list2)
    if length1 < 7 and length2 < 7:
        return render(request, 'MedBrat-project/index.html', {
            'maqolas':list1,
            'dori':list2,
        })
    elif length1 >= 7 and length2 < 7:
        return render(request, 'MedBrat-project/index.html', {
            'maqolas':list1[:6],
            'dori':list2,
        })
    elif length1 < 7 and length2 >= 7:
        return render(request, 'MedBrat-project/index.html', {
            'maqolas':list1,
            'dori':list2[:6],
        })
    elif length1 >=7 and length2 >= 7:
        return render(request, 'MedBrat-project/index.html', {
            'maqolas': list1[:6],
            'dori': list2[:6],
        })

def dorilar_view(request):
    tabletka = Post_tabletkas.objects.all()
    return render(request,'MedBrat-project\sreach.html',{
        'dorilar':tabletka,
    })

def maqolalar_view(request):
    all_maqola = Post_maqolas.objects.all()
    hamshira = Xamshira.objects.filter(paid=True)
    post_hamshira = Post_maqolas.objects.filter(author__in=hamshira)
    list1 = []
    for i in post_hamshira:
        list1.append(i)
    for i in all_maqola:
        if i not in list1:
            list1.append(i)
    return render(request, 'MedBrat-project/post.html', {'all_maqola': list1})



