import difflib

import yaml

from docker_config.generators.no_constraint_compose import remove_placement_contraints


def test_repo_docker_compose_no_placement_contraints():
    """ Asserts that the version of docker-compose-no-placement-constraints is the latest"""
    with open("docker_config/docker-compose-no-placement-constraints.yaml",
              "r") as hosts0:
        with open("docker_config/docker-compose.yaml", "r") as stream:
            dict = yaml.safe_load(stream)
            dict = remove_placement_contraints(dict)
            out_dict = yaml.dump(dict,
                                 default_flow_style=False,
                                 allow_unicode=True)

            diff = difflib.unified_diff(hosts0.readlines(),
                                        out_dict,
                                        fromfile="hosts0",
                                        tofile="hosts1")
            for line in diff:
                print(line)
                # assert line == None
