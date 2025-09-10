import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for image URL
    url = input("Please enter the image URL: ")

    try:
        # Make sure the folder exists
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # check for HTTP errors

        # Only save if it's actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print("✗ The provided URL is not an image.")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Fallback filename if URL has none
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent overwriting if same image already exists
        if os.path.exists(filepath):
            print(f"✗ The image {filename} already exists, skipping download.")
            return

        # Save image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
