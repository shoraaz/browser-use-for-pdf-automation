import asyncio
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI

load_dotenv()  # Ensure OPENAI_API_KEY is set

async def download_kotak_pdfs():
    agent = Agent(
        task=(
            "Visit https://www.kotaklife.com/how-do-i/brochure-savings-and-investments, "
            "scroll through the 'Savings & Investments Plans', "
            "click each 'Download' link, "
            "and download the PDF files."
        ),
        llm=ChatOpenAI(model="gpt-4o"),
        # Optional: enable vision for locating links on varying layouts
        use_vision=True,
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(download_kotak_pdfs())
