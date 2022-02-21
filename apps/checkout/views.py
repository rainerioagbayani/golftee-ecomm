from django.contrib import messages
from django.shortcuts import redirect
from oscar.apps.checkout import views
from oscar.apps.payment import forms, models

from paypal.payflow import facade


class PaymentDetailsView(views.PaymentDetailsView):
    """
    An example view that shows how to integrate BOTH PayPal Express
    (see `get_context_data method`) and PayPal Flow (the other methods).
    Naturally, you will only want to use one of the two.
    """
    template_name = 'checkout/payment_details.html'
    template_name_preview = 'checkout/preview.html'

    def get_context_data(self, **kwargs):
        """
        Add data for Paypal Express flow.
        """
        # Override method so the bankcard and billing address forms can be
        # added to the context.
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        ctx['bankcard_form'] = kwargs.get(
            'bankcard_form', forms.BankcardForm())
        ctx['billing_address_form'] = kwargs.get(
            'billing_address_form', forms.BillingAddressForm())
        return ctx

