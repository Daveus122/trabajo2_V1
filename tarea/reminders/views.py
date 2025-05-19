from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Reminder
from django import forms

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['content', 'important']

    def clean_content(self):
        content = self.cleaned_data['content']
        if not content or not isinstance(content, str) or not content.strip() or len(content.strip()) > 120:
            raise forms.ValidationError("El recordatorio debe ser un texto no vacío de máximo 120 caracteres")
        return content.strip()

def reminder_list(request):
    reminders = Reminder.objects.all()
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Recordatorio creado")
            return redirect(reverse('reminder_list'))
        else:
            messages.error(request, "El recordatorio debe ser un texto no vacío de máximo 120 caracteres")
    else:
        form = ReminderForm()
    return render(request, 'reminders/index.html', {'reminders': reminders, 'form': form})

def update_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == "POST":
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            messages.success(request, "Recordatorio actualizado")
            return redirect(reverse('reminder_list'))
        else:
            messages.error(request, "El recordatorio debe ser un texto no vacío de máximo 120 caracteres")
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/update.html', {'form': form, 'reminder': reminder})

def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == "POST":
        reminder.delete()
        messages.success(request, "Recordatorio borrado")
        return redirect(reverse('reminder_list'))
    return render(request, 'reminders/delete.html', {'reminder': reminder})