from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def main() -> None:
    agent = create_agent(
        model="deepseek-flash",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "What's the weather in San Francisco?"}
            ]
        }
    )

    for msg in result["messages"]:
        print(f"[{msg.type}] {msg.content_blocks}")


if __name__ == "__main__":
    main()
