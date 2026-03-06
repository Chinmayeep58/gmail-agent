import re

def extract_company(subject, sender):

    # try subject first
    match = re.search(r"apply(?:ing)? to ([A-Za-z0-9& ]+)", subject.lower())

    if match:
        return match.group(1).strip().title()

    # fallback to sender domain
    match = re.search(r'@([A-Za-z0-9\-]+)\.', sender)

    if match:
        domain = match.group(1)

        bad_domains = ["gmail", "mail", "noreply", "alerts"]

        if domain.lower() not in bad_domains:
            return domain.capitalize()

    return None