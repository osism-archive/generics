import os
import sys

import jinja2
import yaml

with open(".information.yml") as fp:
    information = yaml.load(fp)

loader = jinja2.FileSystemLoader(searchpath="")
environment = jinja2.Environment(loader=loader, keep_trailing_newline=True)

template = environment.get_template(sys.argv[1])
result = template.render({
    "docker_image_name": information.get("docker_image_name", "NONE"),
    "readme_note": information.get("readme_note", None),
    "versions": information.get("versions", ["latest"])
})
with open(sys.argv[1], "w+") as fp:
    fp.write(result)
