from mysql_config.WebMonitoring.generators.website.tests.website_expected_size import (
    EXPECTED_DAILY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE,
    EXPECTED_WEEKLY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE,
    EXPECTED_MONTHLY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE,
)
from mysql_config.WebMonitoring.generators.website.tests.website_expected_time import (
    EXPECTED_DAILY_WEBSITE_GENERATE_SAMPLES_QUERIES,
    EXPECTED_WEEKLY_WEBSITE_GENERATE_SAMPLES_QUERIES,
    EXPECTED_MONTHLY_WEBSITE_GENERATE_SAMPLES_QUERIES,
)
from mysql_config.WebMonitoring.generators.website.website_generate_samples_queries import (
    website_generate_samples_queries, )
from mysql_config.WebMonitoring.generators.website.website_generate_samples_queries_size import (
    website_generate_samples_queries_size, )


def test_website_generate_samples_queries(capfd):
    website_generate_samples_queries("daily")
    out, _ = capfd.readouterr()
    assert out == EXPECTED_DAILY_WEBSITE_GENERATE_SAMPLES_QUERIES

    website_generate_samples_queries("weekly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_WEEKLY_WEBSITE_GENERATE_SAMPLES_QUERIES

    website_generate_samples_queries("monthly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_MONTHLY_WEBSITE_GENERATE_SAMPLES_QUERIES


def test_website_generate_samples_queries_size(capfd):
    website_generate_samples_queries_size("daily")
    out, _ = capfd.readouterr()
    assert out == EXPECTED_DAILY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE

    website_generate_samples_queries_size("weekly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_WEEKLY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE

    website_generate_samples_queries_size("monthly")
    out, err = capfd.readouterr()
    assert out == EXPECTED_MONTHLY_WEBSITE_GENERATE_SAMPLES_QUERIES_SIZE
