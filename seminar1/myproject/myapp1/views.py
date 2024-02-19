from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logger.info('Открыта начальная страница')
    return render(request,
                  'index.html')

def about(request):
    logger.info('Открыта страница обо мне')
    return render(request,
                  'about.html')