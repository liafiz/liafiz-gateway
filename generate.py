import csv
import os

GO_FOLDER = "go"

# HTML template untuk redirect
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={url}">
<title>Redirecting...</title>
<style>
    body {{
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
    }}
</style>
</head>
<body>
    <p>Mengarahkan ke: <a href="{url}">{url}</a></p>
</body>
</html>
"""

def generate_redirect(slug, url):
    """Generate satu file HTML berdasarkan slug + URL"""
    file_path = os.path.join(GO_FOLDER, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(url=url))
    print(f"Generated: {file_path}")

def main():
    # Pastikan folder go ada
    if not os.path.exists(GO_FOLDER):
        os.makedirs(GO_FOLDER)

    # Baca data dari links.csv
    with open("links.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            slug = row["slug"].strip()
            url = row["url"].strip()
            generate_redirect(slug, url)

if __name__ == "__main__":
    main()
