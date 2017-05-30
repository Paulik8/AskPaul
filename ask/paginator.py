from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PaginatorClass():
	def paginate(self, data, page):
		paginator = Paginator(data, 1)
		try:
			paginator = paginator.page(page)
		except PageNotAnInteger:
			paginator = paginator.page(1)
		except EmptyPage:
				paginator = paginator.page(paginator.num_pages)
		return paginator
