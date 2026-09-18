from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="chat-bison-001", temperature=0.2)
print(llm.predict("Write a short poem about the sea."))