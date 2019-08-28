from django.shortcuts import render

from django.core.mail import send_mail


def contact_index(request):
    company_mail = "anishpratheepan@gmail.com"
    if request.method == "POST":
        name = request.POST.get("name")
        user_email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        # Send a mail to the user
        send_mail(
            str(subject),
            str("From " + name + " ,\n\n\t" + message),
            str(user_email),
            [str(company_mail)],
        )
    return render(request, 'contact/index.html')
