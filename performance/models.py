from django.db import models

class Algorithm(models.Model):
    algorithm_id = models.AutoField(primary_key=True)
    algorithm_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.algorithm_id) + '_' + self.algorithm_name

class Cluster(models.Model):
    cluster_id = models.AutoField(primary_key=True)
    cluster_name =  models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return str(self.cluster_id) + '_' + self.cluster_name


class Performance(models.Model):
    id = models.AutoField(primary_key=True)
    ps_cluster_id = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name='ps_cluster_id')
    number_of_ps = models.IntegerField()
    worker_cluster_id = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name='worker_cluster_id')
    number_of_worker = models.IntegerField()
    algorithm_id = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    accuracy = models.FloatField()
    time = models.FloatField()
    DISTRIBUTED_MANNER_CHOICES = (('data paralel', 'data paralel'), ('model paralel', 'model paralel'))
    distributed_manner = models.CharField(max_length=100, choices= DISTRIBUTED_MANNER_CHOICES, default='data paralel')


    def __str__(self):
        return str(self.id) + '_' + str(self.algorithm_id)