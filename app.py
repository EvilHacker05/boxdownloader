from flask import Flask, request, send_file
import requests

app = Flask(__name__)

@app.route('/<path:target>')
def get_file(target):
    url = request.args.get('target')
    if not url:
        return "No target URL provided. Use: /?target=https://example.com/file.mp4", 400

    # Fetch the file from the target URL
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Serve the file as a download
        return send_file(
            filename_or_file=response.raw,
            as_attachment=True,
            download_name=url.split("/")[-1]
        )
    else:
        return f"Failed to fetch file. Status code: {response.status_code}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
