# generics

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

![Workflow](https://raw.githubusercontent.com/osism/generics/master/images/workflow.png)

## Templates for new projects

* Ansible: https://github.com/osism/ansible-template
* Docker: https://github.com/osism/docker-template

## Manual trigger

An automatic sync is performed every night. This can be started manually with the
following call.

```
REPOSITORY=osism/ansible-hosts
TOKEN=Personal_Access_Token

curl -X POST -H "Authorization: Bearer $TOKEN" \
    -H 'Accept: application/vnd.github.everest-preview+json' \
    "https://api.github.com/repos/$REPOSITORY/dispatches" \
    -d '{"event_type": "sync-with-generics-repository"}'
```
