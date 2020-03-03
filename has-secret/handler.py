def handle(req):
    webhook_url = None
    with open("/var/openfaas/secrets/incoming-webhook-url") as webhook_url_text:
        webhook_url = webhook_url_text.read().strip()

    print(webhook_url)
