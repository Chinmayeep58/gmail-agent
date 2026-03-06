def is_job_email(subject, snippet):

    text = (subject + " " + snippet).lower()

    job_phrases = [
        "thank you for applying",
        "application received",
        "your application has been submitted",
        "we received your application",
        "thanks for applying",
        "application confirmation"
    ]

    for phrase in job_phrases:
        if phrase in text:
            return True

    return False