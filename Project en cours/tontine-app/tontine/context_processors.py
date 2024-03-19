from .models import InformationEntreprise

def enterprise_info(request):
    try:
        enterprise_data = InformationEntreprise.objects.first()  # Adjust query as needed
    except InformationEntreprise.DoesNotExist:
        enterprise_data = None

    return {'enterprise_info': enterprise_data}
