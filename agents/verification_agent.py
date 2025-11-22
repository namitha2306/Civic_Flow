def verify_sources(sources):
    trusted_domains = [".gov.in", ".nic.in"]
    verified, unverified = [], []

    for src in sources:
        if any(domain in src for domain in trusted_domains):
            verified.append(src)
        else:
            unverified.append(src)

    verification_report = {
        "verified_sources": verified,
        "unverified_sources": unverified,
        "confidence": len(verified) / len(sources) if sources else 0
    }
    return verification_report
