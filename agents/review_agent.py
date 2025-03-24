import os
from typing import Dict, List

class ReviewAgent:
    def __init__(self):
        self.review_criteria = {
            "structure": ["headings", "paragraphs", "flow"],
            "content": ["clarity", "accuracy", "engagement", "word_count"],
            "seo": ["keywords", "meta_description", "readability", "links"]
        }

    def analyze_content(self, content: str) -> Dict[str, List[str]]:
        """Analyzes blog content based on multiple criteria."""
        feedback = {
            "strengths": [],
            "improvements": [],
            "seo_suggestions": []
        }

        # Word count analysis
        word_count = len(content.split())
        if word_count >= 1800:
            feedback["strengths"].append("✅ Content meets length requirement ({word_count} words)")
        else:
            feedback["improvements"].append(f"❌ Content length ({word_count} words) below target of 2000 words")

        # Structure analysis
        paragraphs = content.split('\n\n')
        if len(paragraphs) > 5:
            feedback["strengths"].append("✅ Good paragraph separation and structure")
        else:
            feedback["improvements"].append("❌ Need better content structure with more paragraphs")

        # Heading analysis
        heading_count = content.count('#')
        if heading_count > 3:
            feedback["strengths"].append("✅ Good use of headings for content organization")
        else:
            feedback["improvements"].append("❌ Add more section headings for better readability")

        # SEO analysis
        keywords = ['hr', 'human resources', 'workplace', 'employees']
        for keyword in keywords:
            count = content.lower().count(keyword)
            if count > 3:
                feedback["strengths"].append(f"✅ Good keyword density for '{keyword}'")
            else:
                feedback["seo_suggestions"].append(f"❌ Increase usage of keyword '{keyword}'")

        # Links analysis
        if 'http' in content:
            feedback["strengths"].append("✅ Contains external references/links")
        else:
            feedback["seo_suggestions"].append("❌ Add relevant external links for better SEO")

        return feedback

    def generate_review(self, feedback: Dict[str, List[str]]) -> str:
        """Generates a detailed review report in Markdown format."""
        review = """# Blog Content Review

## Summary
This review analyzes the blog content across multiple dimensions including structure, content quality, and SEO optimization.

"""
        for category, items in feedback.items():
            review += f"\n## {category.upper()}\n"
            if items:
                review += "\n".join(items) + "\n"
            else:
                review += "_No specific feedback in this category_\n"

        review += "\n## Overall Recommendations\n"
        if feedback["improvements"] or feedback["seo_suggestions"]:
            review += "Please address the improvement points and SEO suggestions above to enhance the content quality.\n"
        else:
            review += "The content meets all major quality criteria. Good job!\n"

        return review

def main():
    try:
        with open("outputs/final_blog.txt", "r", encoding="utf-8") as file:
            content = file.read()
            
        reviewer = ReviewAgent()
        feedback = reviewer.analyze_content(content)
        review = reviewer.generate_review(feedback)
        
        with open("outputs/review.txt", "w", encoding="utf-8") as file:
            file.write(review)
            
        print("✅ Blog review completed and saved!")
        
    except FileNotFoundError:
        print("❌ Error: final_blog.txt not found! Run content generator first.")
    except Exception as e:
        print(f"❌ Error during review: {str(e)}")

if __name__ == "__main__":
    main()
