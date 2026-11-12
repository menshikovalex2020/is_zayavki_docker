from django.shortcuts import render, redirect
from .models import Zapros
from .forms import ZaprosForm

def zapros_list(request):
    if request.method == 'POST':
        form = ZaprosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zapros_list')
    else:
        form = ZaprosForm()

    zaprosy = Zapros.objects.all().order_by('-created_at')
    
    return render(request, 'zayavki_app/zapros_list.html', {
        'form': form,
        'zaprosy': zaprosy
    })
