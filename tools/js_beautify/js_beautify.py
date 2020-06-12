# This is a deprecated script
# Consult README.md

import os

import jsbeautifier

opts = jsbeautifier.default_options()
opts.indent_size = 2
""" Simple script for beautifying JS code """


def jsbeautifier_driver():
    # Set options

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".js"):
                print(os.path.join(root, file))

                full_path = os.path.join(root, file)
                res = jsbeautifier.beautify_file(full_path, opts)

                with open(full_path, "w") as f:
                    f.write(res)


if __name__ == "__main__":
    jsbeautifier_driver()
