from agents.research_agent import research_query
from agents.summarizer_agent import summarize_snippets
from agents.verification_agent import verify_sources
from agents.reviewer_agent import review_response

def run_workflow(user_query):
    # Stage 1: Research
    snippets = research_query(user_query)
    sources = [s.get("link") for s in snippets if s.get("link")]

    # Stage 2: Summarization
    summary = summarize_snippets(snippets)

    # Stage 3: Verification
    verification = verify_sources(sources)
    confidence = verification["confidence"]

    # Stage 4: Review
    review = review_response(summary)
    clarity = review["clarity_score"]
    accuracy = review["accuracy_score"]

    # Stage 5: Feedback loop
    if confidence < 0.5 or clarity < 0.7:
        # Retry summarization if output is weak
        summary = summarize_snippets(snippets)

    return {
        "final_text": summary,
        "sources": verification["verified_sources"],
        "review": review
    }
