# Ansible role osism.{{ ansible_collection_name }}.{{ ansible_role_name }}
{% for release in releases %}
![Ansible {{ release }}](https://img.shields.io/badge/Ansible-{{ release }}-green.png?style=flat)
{%- endfor %}
{%- for distribution in distributions %}
![{{ DISTRIBUTIONS[distribution]['name'] }}](https://img.shields.io/badge/{{ DISTRIBUTIONS[distribution]['name']|replace(" ", "-") }}-orange.png?style=flat)
{%- endfor %}

Notes
-----

{{ readme_note }}{% endif %}
