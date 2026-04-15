import asyncio
import time
from django.http import HttpResponse

async def http_call_async(request):
    inicio = time.time()

    contador = []
    
    for num in range(1, 6):
        await asyncio.sleep(1)  # espera 1 segundo
        contador.append(f"{num} segundo(s)")
        print(num)

    fim = time.time()
    tempo_total = round(fim - inicio, 2)

    resposta = f"""
    Contagem: {", ".join(contador)} <br>
    Tempo total: {tempo_total} segundos
    """

    return HttpResponse(resposta)