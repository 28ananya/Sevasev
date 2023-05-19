from django.shortcuts import render
import mysql.connector as sql
ph=''
pwd=''
# Create your views here.
def loginaction(request):
    global pwd,ph
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='Ananya@2808',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():

           if key=="phone_no":

            ph=value
           if key=="password":
            pwd=value
            
            
        c="select * from users1 where phone_no='{}' and password='{}'".format(ph,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall()) 
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"welcome.html")
    return render(request,'login_page.html')
