from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import  *
from user.models import Occupation,Xamshira,User,Hospitals
import datetime


# Create your views here.



def singin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        auth = authenticate(request, email=email, password=password)
        auth = User.objects.get(email=email, password=password)
        login(request,auth)

        return redirect('chat',pk=1)

    else:
        return render(request, 'filter/singup.html', {})


@login_required
def chat(request, pk):
    chat_chat = Chat.objects.get(id=pk)

    return render(request, 'filter/chat.html', {
        'chat':chat_chat
    })


def add_chat(request):
    to = request.POST['to']
    to1 = Chat.objects.get(id = to)
    if to1.is_closed == False:
        from_ = request.user
        text = request.POST['text']
        message = Messages.objects.create( from_user=from_, text=text)
        to1.messages.add(message)
    return redirect('chat', pk = to1.id)


# def xamshira_login(request):
#     medicine = Hospitals.objects.all()
#     occupations = Occupation.objects.all()
#     return render(request,'filter/xamshira_login.html',{
#         'medicine':medicine,
#         'occupations':occupations
#     })

# def xamshira_add(request):
#     full_name = request.POST['full_name']
#     email = request.POST['email']
#     password = request.POST['password']
#     paspost = request.POST['pasport']
#     medicine = request.POST['medicine']
#     shifoxona = Hospitals.objects.get(id=medicine)
#     main_nurse_hospital = shifoxona.main_nurse
#     cridit_card = shifoxona.cridit_card
#     user,get = User.objects.get_or_create(username=full_name,email=email,password=password,
#                                           cridit_card=cridit_card)
#     minut_10 = request.POST['10_minut']
#     minut_20 = request.POST['20_minut']
#     occupation = request.POST['occupation']
#     auth = authenticate(request, user=user)
#     user1,get = Xamshira.objects.get_or_create(user=user,shifoxona_id=medicine,kasb_id=occupation,
#                                                pasport=paspost,minut_10 = minut_10,minut_20=minut_20)
#     Notification.objects.create(
#         text=f'@{full_name} Sizning shifoxonangizga xamshira bo`lib ishga kirdi',
#         xamshira=user1,
#         to_user=main_nurse_hospital.user
#     )
#
#     login(request,user)
#     return redirect('chat',pk=1)

def time(request):
    if request.method == "POST":
        id = request.POST['nurse']
        data = request.POST['data']
        time_type = request.POST['time_type']
        return redirect('times', pk=id,data=data,type=time_type)
    else:
        medicine = Hospitals.objects.all()
        occupations = Occupation.objects.all()
        nurse = Xamshira.objects.all()
        # for i in range(1, 61):
        #     Time.objects.create(name=i)

        return render(request,'MedBrat-project/band-etmoq1.html',{
            'medicine':medicine,
            'occupations':occupations,
            'nurse':nurse,
            'time':Time.objects.all()
        })

def times(request,pk,data,type):
    times_in = Time.objects.all()
    nurse = Xamshira.objects.get(id=pk)
    if type == 'short':
        data1 = Check_time.objects.filter(date= data,user_id=pk)
        list1 = []
        for i in data1:
            list1.append(i.vaqt.id)

        return render(request,'filter/time.html',{
            'nurse':nurse,
            'times':times_in,
            'booked':list1,
            'date':data,
            'pk_id':pk,
            'type': 'short'
        })
    else:
        times_in = Time.objects.all()
        data1 = Check_time.objects.filter(date=data, user_id=pk)
        list3 = []
        for i in times_in:
            list3.append(i)
        list1 = []
        list2 = []
        for i in data1:
            list1.append(i.vaqt.id)
        for i in list3:
            index = list3.index(i)
            print(index,list3)
            if i.id not in list1:
                if list3[index+1].id not in list1:
                    list2.append(['yashil',i,list3[index+1]])
                    list3.pop(int(index)+1)
                else:
                    list2.append(['qizil', i, list3[index + 1]])
                    list3.pop(int(index)+1)
            else:
                list2.append(['qizil', i, list3[index + 1]])
                list3.pop(int(index)+1)

        return  render(request,'filter/time.html',{
            'nurse':nurse,
            'times':list2,
            'booked':list1,
            'date':data,
            'pk_id':pk,
            'type':'long'
        })
def time_data_add(request,pk):
    data = request.POST['DATA']
    id = request.POST['pk_id']
    nurse = Xamshira.objects.get(id=id)
    vaqt = Time.objects.get(id=pk)
    try:
        user =Check_time.objects.get(date=data,user=nurse,from_user_check_id=request.user.id)
        user.vaqt = vaqt
        user.save()
    except:
        # if nurse.minut_10 >0:
            # Transactions.objects.create(from_card=request.user.cridit_card,to_card=nurse.user.cridit_card,
            #                             summ=nurse.minut_10,to_us=int(int(nurse.minut_10)*0.1),
            #                             from_user=request.user)
        user =Check_time.objects.create(date=data,user=nurse,vaqt=vaqt,from_user_check=request.user)
    return redirect('times',pk=id,data=data,type='short')


def time_data_add2(request,pk1,pk2):
    data = request.POST['DATA']
    id = request.POST['pk_id']
    nurse = Xamshira.objects.get(id=id)
    vaqt1 = Time.objects.get(id=pk1)
    vaqt2 = Time.objects.get(id=pk2)
    try:
        user =Check_time.objects.filter(date=data,user=nurse,from_user_check_id=request.user.id)
        for i in user:
            i.delete()
        user =Check_time.objects.create(date=data,user=nurse,vaqt=vaqt1,from_user_check_id=request.user.id)
        user =Check_time.objects.create(date=data,user=nurse,vaqt=vaqt2,from_user_check_id=request.user.id)
    except:
        if nurse.minut_10 > 0:
            Transactions.objects.create(from_card=request.user.cridit_card, to_card=nurse.user.cridit_card,
                                        summ=nurse.minut_10, to_us=int(int(nurse.minut_10) * 0.1),
                                        from_user=request.user)

        user = Check_time.objects.create(date=data, user=nurse, vaqt=vaqt1, from_user_check_id=request.user.id)
        user = Check_time.objects.create(date=data, user=nurse, vaqt=vaqt2, from_user_check_id=request.user.id)
    return redirect('times',pk=id,data=data,type='long')

def chatting(request):
    if request.method == 'POST':
        id = request.POST['occupation']
        savol = request.POST['savol']
        nurses = Xamshira.objects.filter(kasb_id=id)
        messages, get= Messages.objects.get_or_create(from_user_id=request.user.id, text=savol)
        chat_chat, get = Chat.objects.get_or_create(from_user_id=request.user.id, savol=str(savol))
        text = f'{request.user.username} sizga savol yubordi'
        for i in nurses:
            chat_chat.to_users.add(i)
            nft , het =Notification.objects.get_or_create(text=text,date=datetime.datetime.now(),to_user=i.user,chat=chat_chat)
        chat_chat.messages.add(messages)
        chat_chat.save()
        nft.save()
        return redirect('chat',pk=chat_chat.id)
    else:
        occupations = Occupation.objects.all()
        hospitals= Hospitals.objects.all()
        nurses = Xamshira.objects.all()
        return render(request,'MedBrat-project/band-etmoq2.html',{
            'occupations':occupations,
            'hospitals':hospitals,
            'hamshira':nurses
        })

def Chats(request):
    user = request.user
    try:
        xamshira = Xamshira.objects.get(user_id=user.id)
        chat = Chat.objects.filter(to_users=xamshira)
    except:
        chat = Chat.objects.filter(from_user=user)
    return render(request,'filter/chats.html',{
        'chats':chat
    })

def See(request):
    return render(request,'see.html')
def Seeing(request):
    user = request.user
    xamshira = Xamshira.objects.get(user_id = user.id)
    date = request.POST['date']
    checks = Check_time.objects.filter(date = date,user=xamshira)
    list1 = []
    for i in checks:
        list1.append(i.vaqt)
    times = Time.objects.all()
    return render(request,'filter/seeing.html',{
        "checks":checks,
        'time':list1,
        'times':times
    })

def close_chat(request):
    to = request.POST['to']
    to1 = Chat.objects.get(id = to)
    to1.is_closed = True
    to1.save()

def notification(request):
    notifications = Notification.objects.filter(to_user=request.user)
    return render(request,'filter/notification.html',{
        'notifications':notifications
    })

def delete_xamshira(request,pk):
    Xamshira.objects.delete(id=pk)
    return redirect('')

def statistic(request):

    Xam = Xamshira.objects.get(user=request.user)

    shifoxona = Hospitals.objects.get(main_nurse = Xam)
    xamshiras = Xamshira.objects.filter(shifoxona=shifoxona)
    return render(request,'filter/xamshiras.html',{
        'xamshiras':xamshiras
    })

def static_user(request,pk):
    xamshira = Xamshira.objects.get(id=pk)
    checkin_today = Check_time.objects.filter(user=xamshira,date = datetime.datetime.today())
    chick_month = Check_time.objects.filter(user=xamshira,date__month=datetime.datetime.now().month)
    likes = xamshira.lik
    return render(request, 'filter/statistics_user.html', {
        'today': checkin_today,
        'month':chick_month,
        'xamshira':xamshira
    })
def add_followers(request,pk):
    follower = User.objects.get(id=pk)
    user = request.user
    if user in follower.followers.all():
        follower.followers.remove(user)
    else:
        follower.followers.add(user)

def add_like(request,pk):
    to = request.POST['to']
    mesage = Messages.objects.get(id=pk)
    if request.user in mesage.like.all():
        mesage.like.remove(request.user)
    else:
        mesage.like.add(request.user)
    return redirect('chat',pk=to)
