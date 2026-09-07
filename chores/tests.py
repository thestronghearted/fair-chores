from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.utils import timezone

from .models import Chore, Claim, Vote

User = get_user_model()


class ChoreModelTests(TestCase):
    def setUp(self):
        self.member = User.objects.create_user(username="alex", password="pw")

    def _make_chore(self, **kwargs):
        defaults = {
            "title": "Wash dishes",
            "scheduled_for": timezone.now() + timedelta(days=1),
            "created_by": self.member,
        }
        defaults.update(kwargs)
        return Chore.objects.create(**defaults)

    def test_chore_str_returns_title(self):
        chore = self._make_chore(title="Take out the trash")
        self.assertEqual(str(chore), "Take out the trash")

    def test_recurring_flag_persists(self):
        chore = self._make_chore(is_recurring=True)
        chore.refresh_from_db()
        self.assertTrue(chore.is_recurring)

        once_off = self._make_chore(title="Fix the fence", is_recurring=False)
        once_off.refresh_from_db()
        self.assertFalse(once_off.is_recurring)


class VoteModelTests(TestCase):
    def setUp(self):
        self.member = User.objects.create_user(username="alex", password="pw")
        self.chore = Chore.objects.create(
            title="Mow the lawn",
            scheduled_for=timezone.now() + timedelta(days=1),
            created_by=self.member,
        )

    def test_member_cannot_vote_twice_on_same_chore(self):
        Vote.objects.create(chore=self.chore, member=self.member, points=5)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Vote.objects.create(chore=self.chore, member=self.member, points=8)


class ClaimModelTests(TestCase):
    def setUp(self):
        self.member = User.objects.create_user(username="alex", password="pw")
        self.chore = Chore.objects.create(
            title="Vacuum the living room",
            scheduled_for=timezone.now() + timedelta(days=1),
            created_by=self.member,
        )

    def test_claim_defaults_to_once_and_active(self):
        claim = Claim.objects.create(
            chore=self.chore,
            member=self.member,
            week_start=date.today(),
        )
        self.assertEqual(claim.mode, Claim.ONCE)
        self.assertTrue(claim.is_active)
