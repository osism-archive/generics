# Ansible osism.{{ ansible_role_name }}

[![Build Status](https://travis-ci.org/osism/ansible-{{ ansible_role_name }}.svg?branch=master)](https://travis-ci.org/osism/ansible-{{ ansible_role_name }})
[![Ansible Galaxy](https://img.shields.io/badge/Ansible%20Galaxy-osism.{{ ansible_role_name|replace("-", "--") }}-blue.svg)](https://galaxy.ansible.com/osism/{{ ansible_role_name }}/)
{%- for release in releases %}
![Ansible {{ release }}](https://img.shields.io/badge/Ansible-{{ release }}-green.png?style=flat)
{%- endfor %}
{%- for distribution in distributions %}
![{{ DISTRIBUTIONS[distribution]['name'] }}](https://img.shields.io/badge/{{ DISTRIBUTIONS[distribution]['name']|replace(" ", "-") }}-orange.png?style=flat)
{%- endfor %}

License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author information
------------------

This role was created by [Betacloud Solutions GmbH](https://www.betacloud-solutions.de).
{%- if readme_note %}

Notes
-----

{{ readme_note }}{% endif %}
