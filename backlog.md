# Backlog

Built from [`_docs/plan.md`](_docs/plan.md). Tasks are ordered so each one is
runnable/testable on its own, working bottom-up from data model to UI.

## Task 1: Data models — Chore, Vote, Claim

Add to `chores/models.py`:

- `Chore`: `title`, `description`, `scheduled_for` (datetime), `is_recurring`
  (bool), `created_by` (FK to `User`), `created_at`.
- `Vote`: `chore` (FK), `member` (FK to `User`), `points` (int), one vote per
  member per chore.
- `Claim`: `chore` (FK), `member` (FK to `User`), `mode`
  (`"once" | "ongoing"`), `week_start` (date), `is_active`.

Register all three in `chores/admin.py`. Run `makemigrations` / `migrate`.

## Task 2: Point value on Chore

Add a `point_value` property (or cached field, recomputed on save) on `Chore`
that averages its `Vote.points`. Cover with a unit test: no votes → `None`
(or 0); a few votes → correct average.

## Task 3: Chore list view

A view + template listing all open chores (not fully claimed for once-off,
or not claimed "ongoing" for recurring) with their current point value and
recurring/once-off flag. Requires login.

## Task 4: Add-chore form

A form + view for a logged-in member to create a new chore (title,
description, scheduled_for, is_recurring). Redirects to the chore list.

## Task 5: Voting

On the chore detail page, let a logged-in member submit/update their point
vote for a chore. Recompute and display the average.

## Task 6: Claiming

On the chore detail page, let a member claim an open chore. For recurring
chores, prompt for `mode` ("just this week" / "ongoing"). Once claimed
(and once-off chores are marked done), remove it from the open list.

## Task 7: Protest / reassessment

Let any member protest an active recurring `Claim`'s point value. A
protest deactivates the current point-value consensus and reopens voting
(clears prior `Vote`s for that chore, or marks them superseded — decide
when implementing). Ongoing claims stay assigned to the same member unless
they choose to release it.

## Task 8: Fairness dashboard

A view showing, per household member: total points currently claimed
(sum of active claims' chore point values) vs. their target share
(`total points / number of members`, unless overridden later). Simple
table, no charts needed for v1.

## Task 9: Test coverage pass

Once the above are implemented, review test coverage as a whole: model
behaviour (point averaging, claim states), the voting/claiming/protest
flows end-to-end, and the fairness calculation. Fill any gaps.
