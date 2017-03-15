from django.http import HttpResponse, JsonResponse
from .models import Performance, Cluster, Algorithm
from django.forms.models import model_to_dict
import math
# GET /benchmark?moneyMax=max&time=maxTime&algoId=id
# return `{result:[{"instance_type":,"numberPS":,"numberWorker"},{""}]}`
def index(request):
    return HttpResponse("Hello, world")

def get_all_plan(request):
    max_time = int(request.GET.get('time', -1))
    max_money = int(request.GET.get('moneyMax', -1))
    algo_id = int(request.GET.get('algoId', 0))
    all_plans = Performance.objects.filter(algorithm_id=algo_id, time__lte=max_time)
    results = []
    for plan in all_plans:
        ps_cluster = plan.ps_cluster_id
        worker_cluster = plan.worker_cluster_id
        total_price = (ps_cluster.price + worker_cluster.price) * math.ceil(plan.time)
        if max_money >= total_price:
            result = {}
            result['ps_cluster_name'] = ps_cluster.cluster_name
            result['worker_cluster_name'] = worker_cluster.cluster_name
            result['numberPS'] = plan.number_of_ps
            result['numberWorker'] = plan.number_of_worker
            result['algo_name'] = Algorithm.objects.get(pk=algo_id).algorithm_name
            result['price'] = total_price
            result['time'] = plan.time
            result['accuracy'] = plan.accuracy
            results.append(result)
    return JsonResponse({'result' : results})
