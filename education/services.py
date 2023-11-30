import json
from datetime import datetime, timedelta

import stripe
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def create_payment(amount):
    stripe.api_key = "sk_test_51OHNoNHHie3tZulbAuvMR2R1SdGvmW3hGptxptQ3ct7xcqe6KgkpN2iHpUeLbfUGFTbdf9kmqwcF5dikvRlDGXWY00VbrNWxnk"

    return stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True},
        payment_method='card',
    )


def retrieve_payment(stripe_id):
    stripe.api_key = "sk_test_51OHNoNHHie3tZulbAuvMR2R1SdGvmW3hGptxptQ3ct7xcqe6KgkpN2iHpUeLbfUGFTbdf9kmqwcF5dikvRlDGXWY00VbrNWxnk"
    return stripe.PaymentIntent.retrieve(
        stripe_id,
    )


def set_schedule(*args,**kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name='Block users',
        task='education.tasks.block_user',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
