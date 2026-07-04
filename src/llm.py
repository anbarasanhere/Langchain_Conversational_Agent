from langchain_openai import ChatOpenAI

def load_llm():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        max_tokens = 1000,
        temperature=0
    )

    return llm