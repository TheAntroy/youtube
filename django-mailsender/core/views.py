from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        subject = f"Saran dikirim oleh: {name}"
        recipient = "EMAIL_PENERIMA"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )

        messages.success(
            request,
            f"<span class='font-bold'>Terima kasih!</span> saran anda berhasil dikirim.",
        )

        return redirect("home")

    return render(request, "core/index.html")
