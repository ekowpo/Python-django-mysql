from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Student
from .models import Department
from .models import Lecturer
from .models import Semester
from .models import SemesterCourse
from .models import Course
from .forms import SemesterCreateForm, SemesterModelForm

def SemesterDetails(request):
    all_semesters = Semester.objects.all()
    all_semesterCourse = SemesterCourse.objects.filter()
    template = loader.get_template('students/semester/index.html')
    context = {'all_semesters': all_semesters}
    return HttpResponse(template.render(context,request))


class SemesterView(ListView):
    def get(self,request, *args,**kwargs):
        all_semesters = Semester.objects.all()
        template = loader.get_template('students/index.html')
        context = {'all_semesters': all_semesters}
        return render(request, 'students/index.html', context)


class SemeterDetailView(DetailView):
    queryset = Semester.objects.all()

    def get_context_data(self,*args, **kwargs):
        context =super(SemeterDetailView, self).get_context_data(*args, **kwargs)
        return context

def semester_createview(request):
    form = SemesterModelForm(request.POST or None)
    #form = SemesterCreateForm()
    if request.method=="POST":
      #  form= SemesterCreateForm(request.POST)
        if form.is_valid():
            form.save()
           # obj=Semester.objects.create(
           #   semesterType = form.cleaned_data.get("semester"),
            #    startDate = form.cleaned_data.get("startDate"),
             #   endDate = form.cleaned_data.get("endDate"),
              #   dne = form.cleaned_data.get("dne"))
            return HttpResponseRedirect('/students/')
        if form.errors:
                print (form.errors)
    template_name = 'students/form.html'
    content = {"form": form}
    return render(request, template_name, content)
                


    

class SemesterCreateView(CreateView):
    form_class = SemesterModelForm
    template_name = 'students/form.html'
    success_url = "/students/"


class SemesterUpdateView(UpdateView):
    form_class = SemesterModelForm
    template_name = 'students/form.html'
    success_url = "/students/"

    def get_queryset(self):
        return Semester.objects.all()

    def get_context_data(self,*args, **kwargs):
        context = super(SemesterUpdateView, self).get_context_data(*args, **kwargs)
        return context

class SemesterDeleteView(DeleteView):
    form_class = SemesterModelForm
    template_name = 'students/deleteform.html'
    success_url = "/students/"

    def get_queryset(self):
        return Semester.objects.all()

    def get_context_data(self,*args, **kwargs):
        context = super(SemesterDeleteView, self).get_context_data(*args, **kwargs)
        return context