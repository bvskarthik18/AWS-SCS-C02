secrets_extension_endpoint = "http://localhost:" + \
    secrets_extension_http_port + \
    "/secretsmanager/get?secretId=" + \
    <secret_name>
  
  r = requests.get(secrets_extension_endpoint, headers=headers)
  
  secret = json.loads(r.text)["SecretString"] # load the Secrets Manager response into a Python dictionary, access the secret