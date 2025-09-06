---
title: Live City Mcp
emoji: 👁
colorFrom: purple
colorTo: green
sdk: gradio
sdk_version: 5.44.1
app_file: app.py
pinned: false
license: apache-2.0
short_description: get the weather and latest news on major cities
---

# Live City MCP 🌆

A Gradio-based web application that provides real-time weather information and latest news for major cities around the world using the Tavily Search API.

## 🚀 Features

- **Weather Information**: Get current weather conditions, temperature, and humidity for any city
- **Latest News**: Fetch top 5 recent news articles about cities including politics, economy, and local updates
- **Real-time Search**: Powered by Tavily's advanced search capabilities
- **Clean Interface**: Easy-to-use Gradio web interface with tabbed navigation
- **JSON Output**: Structured data output for easy integration

## 🔗 Live Demo

- **Hugging Face Space**: [https://huggingface.co/spaces/Ninitje/live-city-mcp](https://huggingface.co/spaces/Ninitje/live-city-mcp)
- **GitHub Repository**: [https://github.com/nini1972/live-city-mcp](https://github.com/nini1972/live-city-mcp)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Tavily API key (get it from [https://app.tavily.com/](https://app.tavily.com/))

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nini1972/live-city-mcp.git
   cd live-city-mcp
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   TAVILY_API_KEY=your_tavily_api_key_here
   MOCK_TAVILY=0  # Set to 1 for mock responses during development
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the app:** Open your browser to `http://localhost:7860`

## 📋 Dependencies

- `gradio==5.44.1` - Web interface framework
- `tavily-python==0.7.11` - Tavily Search API client
- `python-dotenv==1.1.1` - Environment variable management

## 🔧 Configuration

### Environment Variables

- `TAVILY_API_KEY`: Your Tavily API key (required)
- `MOCK_TAVILY`: Set to `1` for mock responses during development (optional)

### For Hugging Face Spaces

Set the following secrets in your Space settings:
- `TAVILY_API_KEY`: Your Tavily API key

## 🌐 API Usage

The app provides two main functions:

### Weather Information
```python
get_city_weather_info("Tokyo")
```
Returns structured JSON with weather data including temperature, conditions, and search results.

### News Articles
```python
get_city_news("London")
```
Returns structured JSON with latest news articles, summaries, and source URLs.

## 📁 Project Structure

```
live-city-mcp/
├── app.py              # Main Gradio application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .env               # Environment variables (not committed)
├── .gitignore         # Git ignore file
└── .gradio/           # Gradio cache and logs
```

## 🚀 Deployment

### GitHub Integration
```bash
# Push to GitHub
git add .
git commit -m "your changes"
git push origin main
```

### Hugging Face Spaces
```bash
# Push to HF Space
git push hf main
```

The Hugging Face Space automatically rebuilds when you push changes.

## 🔒 Security Notes

- Never commit API keys to the repository
- Use environment variables or Hugging Face Secrets for sensitive data
- The `.env` file is ignored by git for security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions:
- Open an issue on [GitHub](https://github.com/nini1972/live-city-mcp/issues)
- Check the [Hugging Face Space](https://huggingface.co/spaces/Ninitje/live-city-mcp) for the live demo

## 🔗 Links

- [Tavily API Documentation](https://docs.tavily.com/)
- [Gradio Documentation](https://gradio.app/docs/)
- [Hugging Face Spaces Guide](https://huggingface.co/docs/hub/spaces)