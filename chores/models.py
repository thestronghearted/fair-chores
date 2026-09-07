from django.conf import settings
from django.db import models


class Chore(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    scheduled_for = models.DateTimeField(
        help_text="Date/time the chore is needed."
    )
    is_recurring = models.BooleanField(
        default=False,
        help_text="Recurring (weekly) chore vs. a once-off chore.",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chores_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["scheduled_for"]

    def __str__(self):
        return self.title


class Vote(models.Model):
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE, related_name="votes")
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chore_votes",
    )
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["chore", "member"], name="one_vote_per_member_per_chore"
            )
        ]

    def __str__(self):
        return f"{self.member} voted {self.points} on {self.chore}"


class Claim(models.Model):
    ONCE = "once"
    ONGOING = "ongoing"
    MODE_CHOICES = [
        (ONCE, "Just this week"),
        (ONGOING, "Ongoing until protested"),
    ]

    chore = models.ForeignKey(Chore, on_delete=models.CASCADE, related_name="claims")
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chore_claims",
    )
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default=ONCE)
    week_start = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.member} claimed {self.chore} ({self.mode})"
