def hello(event, context):
    # ❗ FAKE AWS KEY (This will make Gitleaks fail)
    AWS_ACCESS_KEY_ID = "AKIA1234567890ABCD1234"
    return {
        "statusCode": 200,
        "body": "Hello from python demo service!"
    }