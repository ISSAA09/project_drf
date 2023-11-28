import stripe


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
