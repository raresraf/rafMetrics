import io

import yaml


def remove_placement_contraints(dict):
    for service in dict["services"]:
        if dict["services"][service].get("deploy", None):
            dict["services"][service]["deploy"].pop("placement", None)
            if not dict["services"][service].get("deploy", None):
                dict["services"][service].pop("deploy", None)

    return dict


if __name__ == "__main__":
    with open("docker_config/docker-compose.yaml", "r") as stream:
        try:
            dict = yaml.safe_load(stream)

            dict_no_placement_contraints = remove_placement_contraints(dict)
            with io.open(
                    "docker_config/docker-compose-no-placement-constraints.yaml",
                    "w",
                    encoding="utf8",
            ) as outfile:
                yaml.dump(
                    dict_no_placement_contraints,
                    outfile,
                    default_flow_style=False,
                    allow_unicode=True,
                )

        except yaml.YAMLError as exc:
            print(exc)
