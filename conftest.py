from lib.Utils import get_spark_session
import pytest
@pytest.fixture
def spark():
    "Creates a spark session"
    spark_session = get_spark_session('LOCAL')
    yield spark_session
    spark_session.stop()
@pytest.fixture
def expected_results(spark):
    "gives the expected results."
    results_schema = "state string,count int"
    return spark.read.format('csv').schema(results_schema).load('data/test_result/state_aggregrate.csv')