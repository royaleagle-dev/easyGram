from django.shortcuts import render, get_object_or_404, redirect
from phonebook.models import Contact, ActivityLog
from django.views import View
from . forms import QuickAddForm    #django forms
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView

class IndexView(View):

    def post(self, request):
        form = QuickAddForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            contact = Contact(
                firstname = firstname,
                lastname = lastname,
                phone = phone,
                email = email
            )
            save = contact.save()
            print(save)
            if(save == None):
                activity_logger = ActivityLog(activity = f'New Contact Added <{firstname}>')
                activity_logger.save()
                return JsonResponse({'status':'success', 'message':'Contact added successfully'})
            else:
                return JsonResponse({'status':'warning', 'message':'One or more errors occured, Contact cannot be added'})
        else:
            return JsonResponse({'status':'warning', 'message':'A required field is missing, Contact cannot be added'})
            #return render(request, 'phonebook/index.html', {'form':form})
    
    def get(self, request):
        contacts = Contact.objects.filter(trashed = False).order_by('-timestamp')[:10]
        form = QuickAddForm() 

        context = {
            'contacts': contacts,
            'form': form,
        }

        return render(request, 'phonebook/index.html', context)

class TrashView(View):

    def get(self, request):
        trashed_contacts = Contact.objects.filter(trashed = True).order_by('-firstname')
        form = QuickAddForm()
        context = {
            'contacts' : trashed_contacts,
            'form' : form,
        }
        return render(request, 'phonebook/trashed.html', context)
    
    def post(self, request):
        id = request.POST.get('id')
        contact = get_object_or_404(Contact, id=id)
        contact.trashed = True
        save = contact.save()
        if(save == None):
            activity_logger = ActivityLog(activity=f"Moved Contact <{contact.firstname}> to Trash")
            activity_logger.save()
            return JsonResponse({'status':'success', 'message':'Contact moved to trash successfully'})

class LogView(ListView):
    model = ActivityLog
    template_name = 'phonebook/logs.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return ActivityLog.objects.all().order_by('-id')

class DeleteView(View):
    def post(self, request):
        id = request.POST.get('id')
        if(id):
            contact = get_object_or_404(Contact, id=id)
            delete = contact.delete()
            if(delete):
                return JsonResponse({'status':'success', 'message':'Contact deleted successfully'})
            else:
                return JsonResponse({'status':'warning', 'message':'An error occured, Contact cannot be deleted.'})
