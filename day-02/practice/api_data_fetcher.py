import requests
import json


def fetch_posts():
    """
    Fetch posts from JSONPlaceholder API
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Check if API call was successful
    response.raise_for_status()

    return response.json()


def process_posts(posts):
    """
    Extract meaningful information from API response
    """
    processed_data = []

    for post in posts[:5]:  # Limiting to first 5 posts
        processed_data.append({
            "post_id": post["id"],
            "title": post["title"],
            "user_id": post["userId"]
        })

    return processed_data


def save_to_json(data, filename="output.json"):
    """
    Save processed data to a JSON file
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    print("Fetching data from API...")
    posts = fetch_posts()

    print("Processing data...")
    processed_posts = process_posts(posts)

    print("\nProcessed Output:")
    for post in processed_posts:
        print(f"Post ID: {post['post_id']}, User ID: {post['user_id']}")
        print(f"Title: {post['title']}\n")

    save_to_json(processed_posts)
    print("Data successfully saved to output.json")


if __name__ == "__main__":
    main()
