# Web Automation with Browser-Use + OpenRouter

This project demonstrates web automation using the `browser-use` library with OpenRouter LLM models.

---

# Kotak Life PDF Downloader

This project automates the process of downloading all 'Savings & Investments Plans' PDF brochures from the [Kotak Life website](https://www.kotaklife.com/how-do-i/brochure-savings-and-investments).

## Features
- Uses a browser automation agent powered by OpenAI GPT-4o (or Gemini, depending on script).
- Navigates to the brochure page, scrolls through the plans, clicks each 'Download' link, and saves the PDF files.
- Optionally uses vision capabilities to locate download links and browser download icons.

## Requirements
- Python 3.8+
- `pip install -r requirements.txt`
- Set your `OPENAI_API_KEY` in a `.env` file or as an environment variable.

## Usage

1. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run the script:
   ```cmd
   python download_kotak_pdfs.py
   ```
   Or, for Gemini-based script:
   ```cmd
   python main_gemini.py
   ```

## Output
Downloaded PDFs will be saved in the `kotak_pdfs/` or `downloads/` directory.

## File Overview
- `download_kotak_pdfs.py`: Main script for OpenAI-based automation.
- `main_gemini.py`: Alternative script using Gemini.
- `requirements.txt`: Python dependencies.
- `config.ini`, `pyproject.toml`, `uv.lock`: Project configuration files.

## License
MIT License

---

# Original README follows

## Files

- `simple_automation.py` - Basic example based on documentation
- `web_automation_examples.py` - Comprehensive examples with multiple tasks
- `main.py` - Original script with multiple automation scenarios

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get OpenRouter API Key:**
   - Visit [OpenRouter](https://openrouter.ai/)
   - Sign up and get your API key
   - Add it to `.env` file

3. **Configure environment:**
   ```bash
   # Copy the .env file and add your API key
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

## Usage

### Simple Example
```bash
python simple_automation.py
```

### Comprehensive Examples
```bash
python web_automation_examples.py
```

## Available OpenRouter Models

- `anthropic/claude-3.5-sonnet` - Best for complex reasoning
- `openai/gpt-4o` - Latest OpenAI model
- `qwen/qwen-2.5-7b-instruct:free` - Free model option
- `meta-llama/llama-3.1-70b-instruct` - Open source option

## Example Tasks

1. **AI Model Price Comparison** - Compare pricing on OpenRouter
2. **Python Tutorial Search** - Find learning resources
3. **Cryptocurrency Tracking** - Monitor crypto prices
4. **Job Search** - Find Python developer positions
5. **Form Automation** - Fill out web forms
6. **Tech News Research** - Get latest technology news

## Browser-Use Features

- **Automated Navigation** - AI navigates websites intelligently
- **Form Filling** - Automatically fill forms with data
- **Data Extraction** - Extract structured information from pages
- **Price Comparison** - Compare products across websites
- **Content Research** - Gather information from multiple sources

## Troubleshooting

- Ensure your OpenRouter API key is valid
- Check that browser-use is properly installed
- Some websites may block automation - try different sites
- Increase timeout for slow websites
