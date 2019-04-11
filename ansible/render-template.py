import os
import sys

import jinja2
import yaml

DISTRIBUTIONS = {
  'bionic': {
    'image': 'Ubuntu 18.04',
    'name': 'Ubuntu 18.04'
  },
  'xenial': {
    'image': 'Ubuntu 16.04',
    'name': 'Ubuntu 16.04'
  },
}

with open(".information.yml") as fp:
    information = yaml.load(fp)

loader = jinja2.FileSystemLoader(searchpath="")
environment = jinja2.Environment(loader=loader, keep_trailing_newline=True)

template = environment.get_template(sys.argv[1])
result = template.render({
    "ansible_role_name": information.get("ansible_role_name", "NONE"),
    "distributions": information.get("distributions", ["xenial", "bionic"]),
    "DISTRIBUTIONS": DISTRIBUTIONS,
    "molecule_needs_docker": information.get("molecule_needs_docker", False),
    "readme_note": information.get("readme_note", None),
    "travis_decrypt_key": information.get("travis_decrypt_key", "NONE")
})
with open(sys.argv[1], "w+") as fp:
    fp.write(result)
