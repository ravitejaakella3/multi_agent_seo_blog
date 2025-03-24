import os
import json
from research_agent import fetch_trending_hr_topics

def generate_blog_outline():
    """Generates a structured blog outline based on trending HR topics."""

    # Ensure the output folder exists
    os.makedirs("outputs", exist_ok=True)

    # Fetch trending HR topics
    articles = fetch_trending_hr_topics()
    
    if not articles:
        print("❌ No trending HR topics found. Cannot generate an outline.")
        return
    
    # Choose the first trending topic as our blog theme
    main_topic = articles[0]["title"]

    # Define a structured blog outline
    outline = {
        "title": f"{main_topic}: Key Insights & Trends",
        "introduction": "An overview of the latest trends in HR.",
        "sections": [
            {"heading": "1️⃣ Introduction", "content": "Background of the topic and why it matters."},
            {"heading": "2️⃣ Key Trends", "content": "Discuss the latest trends and insights."},
            {"heading": "3️⃣ Challenges & Solutions", "content": "What are the current challenges in HR?"},
            {"heading": "4️⃣ Future Outlook", "content": "Predictions for the future of HR in this area."},
            {"heading": "5️⃣ Conclusion", "content": "Summarizing key takeaways."}
        ]
    }

    # Save outline as a JSON file
    with open("outputs/blog_outline.json", "w") as file:
        json.dump(outline, file, indent=4)
    
    print("\n✅ Blog outline generated successfully! Saved as 'outputs/blog_outline.json'")

if __name__ == "__main__":
    generate_blog_outline()

