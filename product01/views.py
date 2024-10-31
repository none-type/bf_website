# views.py
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount"))  # amount in cents
        token = request.POST.get("stripeToken")
        
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=token,
                description="Service Payment"
            )

            # Save payment in the database
            Payment.objects.create(
                user=request.user,
                amount=amount / 100,  # Convert cents to dollars
                stripe_charge_id=charge["id"],
            )

            return JsonResponse({"status": "success"})

        except stripe.error.StripeError as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return render(request, "payment_form.html", {"stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY})
