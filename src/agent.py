from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from src.llm import load_llm
from src.prompts import SYSTEM_PROMPT
from src.chat_history import chat_history


llm = load_llm()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chain = prompt | llm

conversation = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history,
    input_messages_key="input",
    history_messages_key="history",
)


def ask_agent(question: str):

    response = conversation.invoke(
        {"input": question}, config={"configurable": {"session_id": "default"}}
    )

    return response.content
