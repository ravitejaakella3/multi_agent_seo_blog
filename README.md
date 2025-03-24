# Multi-Agent SEO Blog Generator

## Overview
An AI-powered system that automatically generates SEO-optimized blog posts using multiple specialized agents. The system handles everything from research to content generation and optimization.

## System Architecture

### Agents
1. **Research Agent**
   - Fetches trending HR topics using NewsAPI
   - Identifies relevant keywords and themes

2. **Content Planning Agent**
   - Creates structured blog outlines
   - Organizes content flow and sections

3. **Content Generation Agent**
   - Utilizes Gemini Pro for content creation
   - Follows SEO best practices
   - Generates ~2000 word articles

4. **SEO Optimization Agent**
   - Optimizes content for search engines
   - Ensures keyword density and meta tags
   - Implements SEO best practices

5. **Review Agent**
   - Proofreads generated content
   - Suggests improvements
   - Ensures quality standards

## Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-agent-seo-blog.git
cd multi-agent-seo-blog
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
copy .env.example .env
```
Add your API keys:
- GEMINI_API_KEY
- NEWS_API_KEY

## Usage

Run the complete pipeline:
```bash
python main.py
```

Or run individual agents:
```bash
python agents/content_planner.py
python agents/content_generator.py
python agents/review_agent.py
python agents/seo_optimizer.py
```

## Project Structure
```
multi_agent_seo_blog/
├── agents/
│   ├── content_planner.py
│   ├── content_generator.py
│   ├── research_agent.py
│   ├── review_agent.py
│   └── seo_optimizer.py
├── models/
│   └── llm_model.py
├── utils/
│   ├── blog_generator.py
│   └── helpers.py
├── data/
│   ├── output.html
│   └── output.md
└── outputs/
    ├── blog_outline.json
    ├── final_blog.txt
    └── seo_blog.txt
```

## Tools & Technologies
- Python 3.8+
- Google Gemini Pro API
- NewsAPI
- JSON for data storage
- HTML/Markdown for output

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License

## Authors
Your Name

## Acknowledgments
- Google Gemini Pro for AI capabilities
- NewsAPI for research data