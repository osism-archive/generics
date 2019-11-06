# OSISM CI scripts and unified templates

Central place for CI scripts and unified templates like README
files.

## Workflow

1. Changes in this repository must first be added to the corresponding template 
   for new projects and successfully verified by the CI.

   The change made in the template must be referenced in the commit message.

2. The change is processed (use of templates, ..) and added to the corresponding
   directories (``docker``, ``ansible``, or ``molecule``).

3. The changes can then be applied to all Ansible role and Docker image repositories
   using [Gilt](https://github.com/metacloud/gilt).

![Workflow](https://raw.githubusercontent.com/osism/travis/master/images/workflow.png)

## Templates for new projects

* Ansible: https://github.com/osism/ansible-template
* Docker: https://github.com/osism/docker-template
