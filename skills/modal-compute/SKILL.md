---
name: modal-compute
description: Use ModalAgent when working with Modal platform data, API resources, provenance, or reproducibility checks from inside BioRouter.
license: Apache-2.0
user-invocable: false
---

# ModalAgent Skill

Use this extension to validate Modal credentials, plan reproducible cloud jobs, and inspect Modal API endpoints. Do not deploy or run jobs without explicit user confirmation.

## Operating rules

- Start with `get_modalagent_status` to confirm whether credentials and base URLs are configured.
- Use `get_modalagent_request_plan` before any endpoint that may create, update, launch, upload, or delete a resource.
- Prefer read-only `GET` requests through `call_modalagent_api` while exploring.
- Do not pass `allow_mutation=true` unless the user has explicitly approved the exact operation, target resource, and expected side effect.
- Preserve platform IDs, versions, owners/authors, timestamps, and URLs in any report.
- Never print API tokens, passwords, bearer headers, or session cookies.

## Useful starting endpoints

- `/apps`
- `/jobs`
- `/secrets`
