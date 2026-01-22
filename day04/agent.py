from error_detector import extract_errors
from llm_agent import analyze_error

LOG_FILE = "logs/app.log"

def main():
    errors = extract_errors(LOG_FILE)

    if not errors:
        print("✅ No errors found")
        return

    print(f"❌ Found {len(errors)} errors\n")

    for idx, error in enumerate(errors, 1):
        print(f"--- Error {idx} ---")
        print(error)
        print("\n🤖 AI Analysis:")
        result = analyze_error(error)
        print(result)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
