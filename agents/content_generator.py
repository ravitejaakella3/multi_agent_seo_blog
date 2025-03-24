import sys 
import os
import json
import google.generativeai as genai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import GEMINI_API_KEY

class ContentGenerator:
    def __init__(self):
        self.model = self._initialize_model()

    def _initialize_model(self):
        """Initialize the Gemini model"""
        if not GEMINI_API_KEY:
            raise ValueError("❌ GEMINI_API_KEY not found!")
        genai.configure(api_key=GEMINI_API_KEY)
        return genai.GenerativeModel("gemini-1.5-pro-latest")

    def load_outline(self):
        """Load blog outline from file"""
        outline_path = "outputs/blog_outline.json"
        if not os.path.exists(outline_path):
            print("❌ No blog outline found! Run content_planner.py first.")
            return None

        try:
            with open(outline_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in blog outline!")
            return None

    def generate_content(self, outline):
        """Generate blog content using the outline"""
        if not outline:
            return None

        prompt = f"""
        Generate a high-quality, SEO-optimized blog post based on the following outline:
        {json.dumps(outline, indent=2)}

        Requirements:
        - Include relevant subheadings (H2 and H3)
        - Maintain a professional but engaging tone
        - Follow SEO best practices (keywords, readability, etc.)
        - Aim for approximately 2000 words
        - Include a compelling introduction and conclusion
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text if response else None
        except Exception as e:
            print(f"❌ Content generation error: {str(e)}")
            return None

    def save_content(self, content, outline):
        """Save content in HTML format"""
        try:
            os.makedirs("outputs", exist_ok=True)
            
            # Save as TXT first (for other agents)
            with open("outputs/final_blog.txt", "w", encoding="utf-8") as file:
                file.write(content)
            
            # Save as HTML
            with open("data/output.html", "r", encoding="utf-8") as template:
                html = template.read()
            
            # Insert content and metadata
            html = html.replace("<title></title>", f"<title>{outline['title']}</title>")
            html = html.replace("<h1></h1>", f"<h1>{outline['title']}</h1>")
            html = html.replace("<!-- Generated content will be inserted here -->", content)
            
            with open("outputs/final_blog.html", "w", encoding="utf-8") as file:
                file.write(html)
            
            print("✅ Blog content generated successfully in TXT and HTML formats!")
            return True
            
        except Exception as e:
            print(f"❌ Error saving blog content: {str(e)}")
            return False

def main():
    generator = ContentGenerator()
    outline = generator.load_outline()
    if not outline:
        return False
    
    content = generator.generate_content(outline)
    if not content:
        return False
    
    return generator.save_content(content, outline)

if __name__ == "__main__":
    main()

