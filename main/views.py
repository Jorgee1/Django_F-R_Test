from django.shortcuts import render
from django.http import HttpResponse


def test(request):
	return HttpResponse('{"msg":"HI"}', content_type='application/json')