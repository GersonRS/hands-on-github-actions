import pytest
from airflow.models import DagBag


def test_dag_integrity():
    dag_bag = DagBag(dag_folder="dags", include_examples=False)
    assert dag_bag.import_erros == {}, "DAGs com erro de importação"
