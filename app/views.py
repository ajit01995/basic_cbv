from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

# Create your views here.


def fbv(request):
    return HttpResponse('This is function base view')


class cbv(View):
    def get(self,request):
        return HttpResponse('this is class base view')
    

class cbvt(TemplateView):
    template_name='cbv.html'
    
