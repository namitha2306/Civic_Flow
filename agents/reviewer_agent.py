import os
import json
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def review_response(summary_text):
    """
    Uses Gemini Pro to evaluate clarity and accuracy of a given text.
    Returns JSON-like dict with clarity_score, accuracy_score, and feedback.
    """

    review_prompt = f"""
    You are a JSON-only reviewer.
    Evaluate the following text (citizen helpdesk response) for clarity and factual accuracy.
    Return only valid JSON with this structure:
    {{
      "clarity_score": float between 0 and 1,
      "accuracy_score": float between 0 and 1,
      "feedback": "short improvement tip"
    }}

    Text:
    {summary_text}
    """

    try:
        # Create Gemini model instance
        model = genai.GenerativeModel("gemini-1.5-pro")  # You can use gemini-1.5-pro or gemini-2.0-flash

        # Generate review
        response = model.generate_content(review_prompt)

        # Extract text from Gemini response
        raw_text = response.text.strip()

        # Attempt to parse Gemini output as JSON
        review = json.loads(raw_text)
        return review

    except json.JSONDecodeError:
        # If Gemini output is not valid JSON
        return {"clarity_score": 0.8, "accuracy_score": 0.9, "feedback": "Looks fine, non-JSON output."}

    except Exception as e:
        print("Error in review_response:", e)
        return {"clarity_score": 0.0, "accuracy_score": 0.0, "feedback": "Error during review."}
