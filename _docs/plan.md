# Plan: Fair Chores

A tool for managing shared household chores, for a household of adults.

## Problem

Chores get done unevenly — someone always ends up doing more than their share,
and it's hard to agree on how much a given chore is actually "worth" compared
to others. This app makes chore effort visible and lets the household agree
on point values democratically, so everyone can see whether the load is
actually split fairly.

## Core Features

### 1. Chore list with point voting

- Any adult household member can add a chore: name, description, and the
  date/time it's needed.
- A chore is flagged as either **recurring** (happens weekly) or **once-off**
  (a single occurrence).
- Household members each cast a point-value vote on a chore. The chore's
  official point value is the average of all votes cast.

### 2. Claiming

- Members claim an open chore from the shared list. Claiming attaches the
  chore's original date/time specs to that member.
- For **recurring** chores, the claimant chooses when claiming:
  - "just this week" (one-off assignment, chore returns to the open pool
    afterward), or
  - "ongoing" (recurs automatically to them every week until someone
    protests it — see below).
- **Once-off** chores are claimed a single time and marked done; they don't
  re-enter a weekly cycle.

### 3. Reassessment / protest

- After a recurring chore's first (trial) week, the claimant can indicate
  whether they agree with its point value.
- Any household member — the claimant or someone else — can protest a
  recurring chore's point value at any time, proposing it be lowered (or
  otherwise reassessed). A protest reopens voting and recomputes the
  average.
- An "ongoing" claim stays in effect for that person until a protest is
  raised against it.

### 4. Fairness tracking

- Each member's target share defaults to an equal split: `1 / (number of
  household members)` of total household chore points.
- A dashboard shows, per member: total points currently claimed (recurring +
  once-off) vs. their target share, so the household can see at a glance who
  is under or over their fair percentage.

## Out of scope (for this homework)

- Notifications/reminders
- Mobile app / native clients
- Multiple households per install (single household per deployment is fine)
- Payment or reward integration

## Tech

- Backend: Django (Python), using `uv` for dependency management
- Auth: Django's built-in user model — one household = one set of registered
  users
- Tests: Django's test runner (`manage.py test`)
