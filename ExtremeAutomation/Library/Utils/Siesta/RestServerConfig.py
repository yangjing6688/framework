class RestServerConfig(object):
    # !!! REQUIRED VALUES
    # !!! Whether HTTPS should be used or not.
    HTTPS = False

    # OPTIONAL VALUES
    # Private key location (only provide if using a non-default private key).
    # PRIVATE_KEY_LOCATION = "ssl.key"

    # Certificate location (only provide if using a non-default certificate).
    # CERTIFICATE_LOCATION = "ssl.cert"

    # To generate private key and certificate.
    # openssl genrsa 2048 > ssl.key
    # openssl req -new -x509 -nodes -sha1 -days 365 -key ssl.key > ssl.cert
