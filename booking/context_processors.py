from barbers_accounts.models import website_salon_details


def logo(request):
    if len(website_salon_details.objects.all()) > 0:
        website_details = website_salon_details.objects.all().last()
    else:
        website_details = []

    return {
        'website_details': website_details
        }

