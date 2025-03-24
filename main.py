import os

def run_pipeline():
    """Executes the full content generation pipeline."""
    os.system("python agents/content_planner.py")
    os.system("python agents/content_generator.py")
    os.system("python agents/review_agent.py")
    os.system("python agents/seo_optimizer.py")
    
    print("✅ Full pipeline executed successfully.")

if __name__ == "__main__":
    run_pipeline()
