import yaml

from docker_config.generators.no_constraint_compose import remove_placement_contraints
from docker_config.generators.tests.mocks import (
    SAMPLE_DOCKER_COMPOSE,
    EXPECTED_DOCKER_COMPOSE,
)


def test_remove_placement_contraints():
    dict = yaml.safe_load(SAMPLE_DOCKER_COMPOSE)
    dict = remove_placement_contraints(dict)
    out_dict = yaml.dump(dict, default_flow_style=False, allow_unicode=True)
    assert out_dict == EXPECTED_DOCKER_COMPOSE
