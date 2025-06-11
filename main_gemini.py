import asyncio
import os
import configparser
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent # Assuming 'browser_use' is your custom library

# --- Configuration Loading ---
def load_configuration():
    """Loads configuration from config.ini and sets the API key."""
    config = configparser.ConfigParser()
    if not os.path.exists('config.ini'):
        raise FileNotFoundError("Error: config.ini file not found. Please create one with your Gemini API key.")
    
    config.read('config.ini')
    
    try:
        api_key = config['gemini']['api_key']
        model_name = config['gemini']['model']
        os.environ["GOOGLE_API_KEY"] = api_key
        print("✅ Configuration loaded successfully.")
        return model_name
    except KeyError:
        raise KeyError("Error: 'gemini' section with 'api_key' and 'model' not found in config.ini.")

async def automate_insurance_brochure_download(model_name: str):
    """
    Automates web browsing to search for life insurance brochures and download them.
    This version uses a more robust prompt for the AI agent.
    """
    # Initialize the browser agent with Gemini
    # The new task prompt is more general and less likely to break.
    agent = Agent(
        task="""
        Your goal is to find and download PDF brochures for 'Kotak Life Insurance'.

        1.  Go to google.com and search for "Kotak Life Insurance brochure PDF".
        2.  Analyze the search results. Click on links that are clearly for a PDF document. These links might end in '.pdf' or have text that says 'PDF'.
        3.  When a PDF is open in the browser's built-in viewer, you must download it. Find and click the 'download' button. This is usually an icon of a downward-pointing arrow.
        4.  Ensure the files are saved into the 'downloads' folder.
        5.  Once you have downloaded one or two brochures, stop and provide a summary of which links you clicked and what files you successfully downloaded.
        """,
        llm=ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.1,
        )
    )
    
    try:
        print("\n🤖 Starting browser automation task...")
        # Run the automation task
        result = await agent.run()
        print("\n✅ Automation Task Completed.")
        print("="*50)
        print("Summary of Results:")
        print(result)
        print("="*50)
        
        return result
        
    except Exception as e:
        print(f"❌ An error occurred during the automation task: {e}")
        return None

async def main():
    """
    Main function to orchestrate the automation.
    """
    print("🚀 Starting Life Insurance Brochure Automation with Gemini")
    
    try:
        model_name = load_configuration()
        
        # Create downloads directory if it doesn't exist
        downloads_dir = "downloads"
        if not os.path.exists(downloads_dir):
            os.makedirs(downloads_dir)
            print(f"📁 Created downloads directory: ./{downloads_dir}")
        else:
            print(f"📁 Downloads directory already exists: ./{downloads_dir}")
            
        await automate_insurance_brochure_download(model_name)

    except (FileNotFoundError, KeyError) as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main asynchronous function
    asyncio.run(main())
