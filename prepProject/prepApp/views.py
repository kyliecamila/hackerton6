from django.shortcuts import render, redirect
from prepApp.models import Subject, Recordings
from datetime import datetime, date
from django.contrib.auth.models import User
import random
# from django.utils import timezone


def home_login(request):
    return render(request, 'home_login.html')

def recordlist(request):

    recordings = Recordings.objects.filter(user=request.user).filter(record = True).order_by('subject_id')
    recordings_num = recordings.count()

    tf = []
    for i in recordings:   
        if i.complete == True:
            tf.append("수강완료")
        else:
            tf.append("미수강")

    
    return render(request, 'recordlist.html', {'recordings': recordings, 'tf': tf})


def checkcomplete(request, pk):
    recording = Recordings.objects.get(pk= pk)
    if request.method =='POST':
        Recordings.objects.filter(pk=pk).update(
            complete = request.POST['complete'],
        )
        return redirect('recordlist')
    return render(request, 'checkcomplete.html', {'recording': recording})

def play(request):
    logged_in_user = request.user
    subjects = Subject.objects.filter(user=request.user)
    num = subjects.count()
   
    if datetime.today().isoweekday()==1:
        subjects1 = subjects.filter(day1 ='월요일')
        subjects2 = subjects.filter(day2 ='월요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                select = request.POST.getlist('record[]').save()
                
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("play2")
        return render(request, 'play.html', {'subjects': subjects})
    if datetime.today().isoweekday()==2:
        subjects1 = subjects.filter(day1 ='화요일')
        subjects2 = subjects.filter(day2 ='화요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("play2")
        return render(request, 'play.html', {'subjects': subjects})
    if datetime.today().isoweekday()==3:
        subjects1 = subjects.filter(day1 ='수요일')
        subjects2 = subjects.filter(day2 ='수요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("play2")
        return render(request, 'play.html', {'subjects': subjects})
    if datetime.today().isoweekday()==4:
        subjects1 = subjects.filter(day1 ='목요일')
        subjects2 = subjects.filter(day2 ='목요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("play2")
        return render(request, 'play.html', {'subjects': subjects})
    if datetime.today().isoweekday()==5:
        subjects1 = subjects.filter(day1 ='금요일')
        subjects2 = subjects.filter(day2 ='금요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                if i == num - 1:
                    return redirect("play2")
       
        return render(request, 'play.html', {'subjects': subjects})
    if datetime.today().isoweekday()==6:
        subjects1 = subjects.filter(day1 ='토요일')
        subjects2 = subjects.filter(day2 ='토요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        for i in range(num):
            if request.method == "POST":
                select = request.POST.getlist('record[]')
                rnum = len(select)
                if i > (rnum - 1) :
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = "False"
                    record_yesno.save()                    
                else:
                    record_yesno = Recordings()
                    record_yesno.subject = subjects[i]
                    record_yesno.record = select[i]
                    record_yesno.save()
                # rnum = len(select)
                # if i > (rnum - 1) :
                #     record_yesno = Recordings()
                #     record_yesno.subject = subjects[i]
                #     record_yesno.record = "False"
                #     record_yesno.save()                    
                # else:
                #     record_yesno = Recordings()
                #     record_yesno.subject = subjects[i]
                #     record_yesno.record = select[i]
                #     record_yesno.save()
                if i == num - 1:
                    return redirect("play2")
       
        return render(request, 'play.html', {'subjects': subjects})
    else:
        return render(request, 'play.html')


            

def play2(request):
    # logged_in_user = request.user
    subjects = Subject.objects.filter(user=request.user)
    records = Recordings.objects.filter(user=request.user).filter(date=datetime.today())
    recordings = records.order_by('subject__start_time')
    travel=['서울','부산','제주도']
    travel_select = random.choice(travel)

    tf = []
    
    for i in recordings:   
        if i.record == True:
            tf.append("녹화")
        else:
            tf.append("녹화 x")
   
    if datetime.today().isoweekday()==1:
        subjects1 = subjects.filter(day1 ='월요일')
        subjects2 = subjects.filter(day2 ='월요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'play2.html', {'subjects': subjects})
    if datetime.today().isoweekday()==2:
        subjects1 = subjects.filter(day1 ='화요일')
        subjects2 = subjects.filter(day2 ='화요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'play2.html', {'subjects': subjects})
    if datetime.today().isoweekday()==3:
        subjects1 = subjects.filter(day1 ='수요일')
        subjects2 = subjects.filter(day2 ='수요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        num = subjects.count()
        return render(request, 'play2.html', {'subjects': subjects})
    if datetime.today().isoweekday()==4:
        subjects1 = subjects.filter(day1 ='목요일')
        subjects2 = subjects.filter(day2 ='목요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'play2.html', {'subjects': subjects})
    if datetime.today().isoweekday()==5:
        subjects1 = subjects.filter(day1 ='금요일')
        subjects2 = subjects.filter(day2 ='금요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'play2.html', {'subjects': subjects})
    if datetime.today().isoweekday()==6:
        subjects1 = subjects.filter(day1 ='토요일')
        subjects2 = subjects.filter(day2 ='토요일')
        subjects = subjects1.union(subjects2).order_by('start_time')
        return render(request, 'play2.html', {'subjects': subjects, 'tf': tf,  
        'recordings': recordings, 'travel_select': travel_select})
    else:
        return render(request, 'play2.html', { 'tf': tf })

    

def study(request):
    # logged_in_user = request.user
    total = Subject.objects.all().count()
    subjects = Subject.objects.filter(user=request.user).order_by('id')
    subject_num = subjects.count()
    my_subject_id =[]

    # my_subject_id[0] = subjects[4].id
    for i in range(total):
        if subject_num < i + 1 :
            break
        else:
            my_subject_id.append(subjects[i].id)
    
# total = 11 subject_num =10
 
    
    #강의 전체 개수 세기
    lectures = Recordings.objects.all()
    lectures_num = Recordings.objects.all().count()
    #녹화한 과목 전체 개수 세기
    recordings = Recordings.objects.filter(record = True)
    recordings_num =recordings.count()
    #수강한 강의 개수
    completed_recordings = Recordings.objects.filter(record = True).filter(complete = True)
    comp_num =completed_recordings.count()


    recording_rate = recordings_num / lectures_num * 100
    complete_rate = comp_num / recordings_num * 100

    sub = []
    in_num = []
    for i in range(subject_num):
        # for j in recordings:
        number = recordings.filter(subject_id = my_subject_id[i]).count() 
        sub.append(number)
   

    incompleted_recordings = recordings.filter(record = True).filter(complete = False)
    for i in range(subject_num):
        # for j in incompleted_recordings:
        number = incompleted_recordings.filter(subject_id = my_subject_id[i]).count() 
        in_num.append(number)

       
# subject_name = "크롤링한 과목"
# if Subject.objects.get(name=subject_name):
#     pass
# else:
#     Subject.objects.create(name=)

    return render(request, 'study.html', {'subjects': subjects, 'lectures_num': lectures_num, 
    'recordings_num': recordings_num,'recording_rate': recording_rate, 'sub': sub,
     'subject_num': subject_num, 'my_subject_id': my_subject_id,
      'in_num': in_num, 'comp_num': comp_num , 'complete_rate': complete_rate })   

