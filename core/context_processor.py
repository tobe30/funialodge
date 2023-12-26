from core.models import Lodges
from django.db.models import Min, Max


def default(request):

    min_max_price = Lodges.objects.aggregate(Min("price"), Max("price"))


    return {
        'min_max_price':min_max_price,
    }
