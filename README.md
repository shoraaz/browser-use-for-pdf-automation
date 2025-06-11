# Web Automation with Browser-Use + OpenRouter

This project demonstrates web automation using the `browser-use` library with OpenRouter LLM models.

---

# PDF Downloader

This project automates the process of downloading all pdf as per user instructions from websites.

## Features
- Uses a browser automation agent powered by OpenAI GPT-4o (or Gemini, depending on script).
- Navigates to the required page, scrolls through the required things, clicks each 'Download' link, and saves the PDF files.
- Optionally uses vision capabilities to locate download links and browser download icons.

## Requirements
- Python 3.8+
- `uv pip install -r requirements.txt`
- Set your `OPENAI_API_KEY` in a `.env` file or as an environment variable.

## Usage

1. Install dependencies:
   ```cmd
   uv pip install -r requirements.txt
   ```
2. Set your OpenAI API key in a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run the script:
   ```cmd
        uv run main.py
   ```
   Or, for Gemini-based script:
   ```cmd
   uv run main_gemini.py
   ```

## Output
Downloaded PDFs will be saved in the `kotak_pdfs/` or `downloads/` directory.



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
