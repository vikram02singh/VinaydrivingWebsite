from django.shortcuts import render, redirect
from django.http import HttpRequest
from urllib.parse import quote

def home(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if name and phone and message:
            whatsapp_number = "919411047482"
            text = (
                f"Hello Vinay Driving School!\n\n"
                f"Name: {name}\n"
                f"Phone: {phone}\n"
                f"Message: {message}"
            )
            wa_link = f"https://wa.me/{whatsapp_number}?text={quote(text)}"
            return redirect(wa_link)

    return render(request, 'main/index.html')
