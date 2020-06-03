# Ansible osism.{{ ansible_role_name }}

[![Build Status](https://travis-ci.org/osism/ansible-{{ ansible_role_name }}.svg?branch=master)](https://travis-ci.org/osism/ansible-{{ ansible_role_name }})
{%- for release in releases %}
![Ansible {{ release }}](https://img.shields.io/badge/Ansible-{{ release }}-green.png?style=flat)
{%- endfor %}
{%- for distribution in distributions %}
![{{ DISTRIBUTIONS[distribution]['name'] }}](https://img.shields.io/badge/{{ DISTRIBUTIONS[distribution]['name']|replace(" ", "-") }}-orange.png?style=flat)
{%- endfor %}

Author information
------------------

This role was created by [Betacloud Solutions GmbH](https://www.betacloud-solutions.de).
{%- if readme_note %}

Notes
-----

{{ readme_note }}{% endif %}
