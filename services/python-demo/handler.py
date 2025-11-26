def hello(event, context):
    # ❗ FAKE AWS KEY (This will make Gitleaks fail)
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    return {
        "statusCode": 200,
        "body": "Hello from python demo service!"
    }