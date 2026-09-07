# Fair Chores

A tool for managing shared household chores. Adults in a household list
chores, vote on how many points each chore is worth, and claim chores from
the shared list. The app tracks each person's claimed points against their
fair share of the total, so everyone can see whether the load is split
evenly.

Built for the [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
Homework 1.

See [`_docs/plan.md`](_docs/plan.md) for the full spec, and `backlog.md`
(once created) for the build plan.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

## Project layout

- `config/` — Django project (settings, URLs)
- `chores/` — Django app: chores, votes, claims, fairness tracking
