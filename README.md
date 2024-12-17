# YouCaption

**YouCaption** is a simple Python tool that allows you to download English subtitles (captions) from YouTube videos and save them into a text file. This app helps you easily capture the transcript from any YouTube video that has subtitles available.

## Features
- Download subtitles from YouTube videos.
- Save subtitles in plain text format without timestamps.
- User-friendly interface with inputs for YouTube video URL and output filename.

## Requirements
- Python 3.x
- `yt-dlp` library for downloading YouTube video info and subtitles.
- `requests` library for handling HTTP requests.

## Installation

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/your-username/YouCaption.git
    cd YouCaption
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

   If you don’t have the `requirements.txt`, manually install the libraries:

    ```bash
    pip install yt-dlp requests
    ```

## Usage

1. Open a terminal or command prompt.

2. Run the Python script:

    ```bash
    python YouCaption.py
    ```

3. When prompted, input the YouTube video URL and the desired output filename for the subtitles.

    Example:
    ```
    Enter the YouTube video URL: https://youtu.be/odFzZWuH0cU
    Enter the output filename (e.g., captions.txt): marineford_captions.txt
    ```

4. The subtitles will be downloaded and saved in the specified file.

## Error Handling
- Invalid YouTube URLs will result in an error message asking for a valid URL.
- If no English subtitles are available, the script will inform the user.
- If the download fails or there’s a problem with the subtitle URL, an error message will be displayed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - A powerful tool for downloading videos and subtitles from YouTube.
- [requests](https://pypi.org/project/requests/) - A simple HTTP library for Python.

