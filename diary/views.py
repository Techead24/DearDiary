from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Entry
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

# user = self.request.user






# Create your views here.
class ELV(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created") #takes all the entries and orders it by date
    template_name = 'entries\entry_list.html'
    

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).order_by("-date_created")

    
    

    
class EDV(DetailView):
    model = Entry
    template_name = 'entries\entry_detail.html'
  
    
    
    

class ECV(CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    template_name = 'entries\entry_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ECV, self).form_valid(form)
            

    
    

class EUV(UpdateView):
    model = Entry
    fields = ["title", "content"]
    template_name = 'entries\entry_update_form.html'
    
    def get_success_url(self):   
         
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )
        

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    template_name = 'entries\entry_delete.html'


def About(request):
    return render(request, 'entries/About.html')