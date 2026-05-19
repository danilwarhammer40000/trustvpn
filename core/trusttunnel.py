import os
import re
import subprocess

from config.settings import (
    VPN_DOMAIN,
    TRUSTTUNNEL_PATH,
)


def validate_domain(
    domain: str
):

    if not domain:
        raise ValueError(
            "empty domain"
        )

    if not re.match(
        r"^[a-zA-Z0-9.-]+$",
        domain
    ):
        raise ValueError(
            "invalid domain"
        )


def generate_link(
    username: str,
):

    validate_domain(
        VPN_DOMAIN
    )

    endpoint = os.path.join(
        TRUSTTUNNEL_PATH,
        "trusttunnel_endpoint"
    )

    fallback = (
        f"https://"
        f"{VPN_DOMAIN}"
        f"/connect/"
        f"{username}"
    )

    if not os.path.isfile(
        endpoint
    ):
        return fallback

    try:

        result = subprocess.run(
            [
                endpoint,

                "vpn.toml",

                "hosts.toml",

                "-c",

                username,

                "-a",

                VPN_DOMAIN,
            ],

            cwd=
            TRUSTTUNNEL_PATH,

            capture_output=True,

            text=True,

            timeout=15,
        )

        output = (
            result.stdout.strip()
        )

        if output:
            return output

        return fallback

    except Exception:

        return fallback
