# docker-{{ docker_image_name }}

[![Build Status](https://travis-ci.org/osism/docker-{{ docker_image_name }}.svg?branch=master)](https://travis-ci.org/osism/docker-{{ docker_image_name }})
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-osism%2F{{ docker_image_name|replace("-", "--") }}-blue.svg)](https://hub.docker.com/r/osism/{{ docker_image_name }}/)

Author information
------------------

This Docker image was created by [Betacloud Solutions GmbH](https://www.betacloud-solutions.de).

Notices
-------

Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the
United States and/or other countries. Docker, Inc. and other parties may also have trademark
rights in other terms used herein.
{%- if readme_note %}

Notes
-----

{{ readme_note }}{% endif %}
