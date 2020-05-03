from mysql_config.WebMonitoring.generators.resource.resource_generate_samples_queries import (
    resource_generate_samples_queries, )
from mysql_config.WebMonitoring.generators.resource.resource_generate_samples_queries_size import (
    resource_generate_samples_queries_size, )
from mysql_config.WebMonitoring.generators.resource.tests.resource_expected_size import (
    EXPECTED_DAILY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE,
    EXPECTED_WEEKLY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE,
    EXPECTED_MONTHLY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE,
)
from mysql_config.WebMonitoring.generators.resource.tests.resource_expected_time import (
    EXPECTED_DAILY_RESOURCE_GENERATE_SAMPLES_QUERIES,
    EXPECTED_WEEKLY_RESOURCE_GENERATE_SAMPLES_QUERIES,
    EXPECTED_MONTHLY_RESOURCE_GENERATE_SAMPLES_QUERIES,
)


def test_resource_generate_samples_queries(capfd):
    resource_generate_samples_queries("daily")
    out, _ = capfd.readouterr()
    assert out == EXPECTED_DAILY_RESOURCE_GENERATE_SAMPLES_QUERIES

    resource_generate_samples_queries("weekly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_WEEKLY_RESOURCE_GENERATE_SAMPLES_QUERIES

    resource_generate_samples_queries("monthly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_MONTHLY_RESOURCE_GENERATE_SAMPLES_QUERIES


def test_resource_generate_samples_queries_size(capfd):
    resource_generate_samples_queries_size("daily")
    out, _ = capfd.readouterr()
    assert out == EXPECTED_DAILY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE

    resource_generate_samples_queries_size("weekly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_WEEKLY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE

    resource_generate_samples_queries_size("monthly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_MONTHLY_RESOURCE_GENERATE_SAMPLES_QUERIES_SIZE
