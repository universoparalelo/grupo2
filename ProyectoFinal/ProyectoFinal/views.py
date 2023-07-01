from django.shortcuts import render


def Home(request):
	return render(request,'inicio.html')

def SegundaPagina(request):
	return render(request,'segundapagina.html')

def TerceraPagina(request):
	return render(request,'tercera.html')