def detect_status(text):

    text = text.lower()

    if "unfortunately" in text or "regret" in text:
        return "Rejected"

    if "interview" in text:
        return "Interview"

    if "assessment" in text or "test" in text:
        return "Assessment"

    if "offer" in text or "congratulations" in text:
        return "Offer"

    if "application received" in text or "thank you for applying" in text:
        return "Applied"

    return "Pending"