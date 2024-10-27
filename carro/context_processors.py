def importe_total_carro (request):  #Tambien hay q registrar la variable ne el setting / TEMPLATES
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total + float(value["precio"])
    
    else:
        total="Debes hacer login"
    
    return{"importe_total_carro":total}
