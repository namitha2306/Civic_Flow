from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_snippets(snippets):
    combined_text = "\n\n".join(
        f"{s['title']}: {s['snippet']}" for s in snippets if s.get("snippet")
    )

    prompt = f"""
    You are a government helpdesk AI assistant.
    Summarize the following official information clearly and simply for a citizen.
    Provide 3–5 sentences and mention steps or links if any.

    {combined_text}
    """

    # ✅ Use your working model
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API Error: {e}"
