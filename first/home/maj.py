import numpy as np;
from . import ann;
from django.http import HttpResponse
from django.shortcuts import render;
def predict(request):
    cs=request.GET['cs'];
    cou=request.GET['cou'];
    gen=request.GET['gen'];
    ag=request.GET['ag'];
    ten=request.GET['ten'];
    bal=request.GET['bal'];
    nop=request.GET['nop'];
    cre=request.GET['cre'];
    act=request.GET['act'];
    est=request.GET['est'];
    ary=np.array([[0,0,cs,gen,ag,ten,bal,nop,cre,act,est]]);
    ary=ann.ss.fit_transform(ary);
    val=ann.cls.predict(ary);
    return render(request,'out.html',{'age':val});
   