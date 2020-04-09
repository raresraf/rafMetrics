import os
import jsbeautifier
""" Simple script for beautifying JS code """


def jsbeautifier_driver():
    # Set options
    opts = jsbeautifier.default_options()
    opts.indent_size = 2

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".js"):
                print(os.path.join(root, file))

                full_path = os.path.join(root, file)
                res = jsbeautifier.beautify_file(full_path, opts)

                with open(full_path, "w") as f:
                    f.write(res)


if __name__ == "__main__":
    jsbeautifier_driver()
