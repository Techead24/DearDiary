from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Entry


# Create your views here.
class ELV(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created") #takes all the entries and orders it by date
    template_name = 'entries\entry_list.html'

    
class EDV(DetailView):
    model = Entry
    template_name = 'entries\entry_detail.html'
    
    

class ECV(CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    template_name = 'entries\entry_form.html'
    

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
    
