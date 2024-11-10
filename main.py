# from file_handler import process_directory
from chat_functions import analyze_file_content


def main():
    # Loop through each file content and analyze
    result = analyze_file_content("content", analysis_type="summary")
    print(f"Result for :\n{result}\n")
if __name__ == "__main__":
    main()
