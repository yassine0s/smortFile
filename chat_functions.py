import openai
from config import OPEN_API_KEY

openai.api_key = OPEN_API_KEY


def query_chatgpt(prompt):
    """Send a prompt to the ChatGPT API and return the response."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error querying ChatGPT: {e}")
        return None


def analyze_file_content(content, analysis_type="summary"):
    """Analyze the content based on the specified analysis type."""
    if analysis_type == "summary":
        # prompt = f"Please summarize the following content:\n\n{content}"
        prompt = f"Please summarize the following content: hello"

    elif analysis_type == "keywords":
        prompt = (
            f"Extract key topics or keywords from the following content:\n\n{content}"
        )
    else:
        prompt = f"Perform {analysis_type} on the following content:\n\n{content}"

    return query_chatgpt(prompt)
