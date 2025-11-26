def hello(event, context):
    # 🚨 Fake Stripe API Key (WILL fail Gitleaks default rules)
    LEAKED_API_KEY = "AKIA1234567890ABCDE" + "F"

    return {
        "statusCode": 200,
        "body": "Hello from python demo service!"
    }