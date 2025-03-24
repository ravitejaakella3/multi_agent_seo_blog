import json

def optimize_seo():
    """Reads the blog content and applies basic SEO optimizations."""
    try:
        with open("outputs/final_blog.txt", "r", encoding="utf-8") as file:
            blog_content = file.read()
        
        # Example SEO Optimization: Replace "AI" with "Artificial Intelligence"
        optimized_content = blog_content.replace("AI", "Artificial Intelligence")
        
        with open("outputs/seo_blog.txt", "w", encoding="utf-8") as file:
            file.write(optimized_content)
        
        print("✅ SEO Optimization completed and saved.")
    except FileNotFoundError:
        print("❌ Error: final_blog.txt not found. Run the content generator first.")
    except UnicodeDecodeError:
        print("❌ Encoding Error: Ensure final_blog.txt is in UTF-8 format.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    optimize_seo()

