from .models import Mensaje

def unread_message_count(request):
    if request.user.is_authenticated:
        unread_count = Mensaje.objects.filter(destinatario = request.user, leido = False).count()
        return {'unread_count': unread_count}
    return {}
