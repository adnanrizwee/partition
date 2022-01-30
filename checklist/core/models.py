from django.db import models

from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel

class Model1(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["timestamp"]

    name = models.TextField()
    timestamp = models.DateTimeField()


class Model2(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["timestamp"]

    model22 = models.ForeignKey(Model1, on_delete=models.CASCADE, null=True,
                                            related_name='model22_Model1')

    name = models.TextField()
    timestamp = models.DateTimeField()


class Model3(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["timestamp"]

    model33 = models.ForeignKey(Model1, on_delete=models.CASCADE, null=True,
                                            related_name='model33_Model1')

    name = models.TextField()
    timestamp = models.DateTimeField()


class Model4(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["timestamp"]

    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE, null=True,
                                                   related_name='model1_Model1')
    model2 = models.ForeignKey(Model2, on_delete=models.CASCADE, null=True,
                                                   related_name='model2_Model2')
    model3 = models.ForeignKey(Model3, on_delete=models.CASCADE, null=True,
                                                   related_name='model3_Model3')
    timestamp = models.DateTimeField()
