import yt_dlp
import requests

# Function to download captions from a YouTube URL
def download_captions(video_url, output_filename):
    ydl_opts = {
        'format': 'best',
        'writesubtitles': True,
        'subtitlelangs': ['en'],  # Specify the language of the subtitles (English in this case)
        'outtmpl': '%(id)s',  # Save subtitles with video ID as filename
        'quiet': True,  # Suppress unnecessary output
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Extracting information from {video_url}...")
            info_dict = ydl.extract_info(video_url, download=False)
            subtitles = info_dict.get('subtitles', {})

            if 'en' in subtitles:  # Check if English subtitles are available
                subtitle_url = subtitles['en'][0]['url']
                print(f"English subtitles found. Downloading from: {subtitle_url}")

                # Use requests to download the subtitle JSON file
                response = requests.get(subtitle_url)

                if response.status_code == 200:
                    subtitle_data = response.json()

                    # Extract and save the transcript
                    with open(output_filename, 'w', encoding='utf-8') as f:
                        print("Saving subtitles...")
                        for line in subtitle_data.get('events', []):
                            if 'segs' in line:
                                for segment in line['segs']:
                                    if 'utf8' in segment:
                                        f.write(segment['utf8'] + '\n')
                    print(f"Captions have been saved to '{output_filename}' successfully!")
                else:
                    print(f"Failed to download subtitles. HTTP Status Code: {response.status_code}")
            else:
                print("No English subtitles available for this video.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the URL and try again.")

# Main function to take YouTube URL and output filename as input
def main():
    print("Welcome to the YouTube Captions Downloader!")
    print("This tool allows you to download English subtitles from YouTube videos.")

    # Get YouTube URL from user input
    video_url = input("Enter the YouTube video URL: ").strip()  

    # Validate YouTube URL format
    if not video_url.startswith("https://youtu.be/") and not video_url.startswith("https://www.youtube.com/"):
        print("Invalid YouTube URL. Please provide a valid URL starting with 'https://youtu.be/' or 'https://www.youtube.com/'.")
        return

    # Get output filename from user input
    output_filename = input("Enter the output filename (e.g., captions.txt): ").strip()

    # Confirm the download
    print(f"\nYou are about to download subtitles from: {video_url}")
    print(f"Subtitles will be saved to: {output_filename}")
    confirm = input("Do you wish to proceed? (yes/no): ").strip().lower()

    if confirm in ['yes', 'y']:
        download_captions(video_url, output_filename)
    else:
        print("Download canceled. Goodbye!")

if __name__ == "__main__":
    main()
