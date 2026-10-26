from openai import OpenAI

from config import MODEL, OLLAMA_BASE_URL
from vector_store import retriever
from prompts import SYSTEM_PROMPT_TEMPLATE


ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama"
)


def chat(message, history):
    docs = retriever.invoke(message)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    system_message = SYSTEM_PROMPT_TEMPLATE.format(
        context=context
    )

    messages = [
        {"role": "system", "content": system_message}
    ] + history + [
        {"role": "user", "content": message}
    ]

    response = ollama.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content