from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ask.models import models

class PaginatorClass():
    def paginate(self, data, page):
	quests = models.Question2.objects.all()
        paginator = Paginator(data, 2)
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
                paginator = paginator.page(paginator.num_pages)
        return render_to_response('pagination.html', {'quests':quests})
