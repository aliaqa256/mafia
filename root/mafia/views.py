from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Player
import random
from django.core.mail import send_mail
from django.conf import settings
email_from = settings.EMAIL_HOST_USER
# Create your views here.
def main(request):
    if request.method =='POST':
        players=request.POST.get("players")
        emails=request.POST.get("emails")
        roles=request.POST.get("roles")
    
        players=players.split(',')
        emails=emails.split(',')        
        roles=roles.split(',')
        if   not ((len(players) == len(roles) ) and   (len(emails) == len(roles) )):
            messages.error(request, 'wrong input')
            return redirect("main:main")



        for i in range(len(players)):
            role=random.choice(roles)

            player = Player.objects.create(name=players[i], role=role,email=emails[i])
            player.save()
                                
            recipient_list = [emails[i],]
            send_mail( "mafia", f"{players[i]} aziz naqshe shoma hast {role}", "mafia@paraiba.com", recipient_list, fail_silently=False)
            roles.remove(role)

    all_players=Player.objects.filter(is_alive=True)
        
            
    return render(request,"mafia/main.html",{"players":all_players})



def clear(request):
    Player.objects.all().delete()
    return redirect("main:main")


def kill(request):
    pk=request.POST.get("pk")
    player=Player.objects.get(pk=pk)
    player.is_alive=False
    player.save()
    return redirect("main:main")


