#!/usr/bin/env python3

import yaml

print("""
<html>
<head>
  <title>Digital Tolkien: Little Delvings</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
      @import url('https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@300&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap');

      .site-header {
        background: #282D34;
        min-height: 56px;
        position: relative;
      }
      .wrapper {
        max-width: calc(800px - (15px * 2));
        margin-right: auto;
        margin-left: auto;
        padding-right: 15px;
        padding-left: 15px;
      }
      .site-title {
        font-size: 26px;
        font-weight: 300;
        line-height: 57.6px;
        margin-bottom: 0;
        float: left;
        text-decoration: none;
        color: #CC9;
      }
      .site-nav {
        float: right;
        line-height: 57.6px;
      }
      .site-nav .page-link {
        margin-right: 20px;
        color: #E8E8E8;
        line-height: 1.6;
        text-decoration: none;
      }
      .page-content {
        padding: 30px 0;
        flex: 1;
      }
      body {
        display: flex;
        min-height: 100vh;
        flex-direction: column;
        margin: 0;
        font-family: "Merriweather", "Georgia", serif;
        box-sizing: border-box;
      }
      .delving {
        margin-top: 8rem;
        max-width: 800px;
      }
      h2 {
        margin-bottom: 0;
      }
      .description {
        font-size: 10pt;
      }
      .code {
        margin-top: 0.5rem;
        font-size: 10pt;
      }
      img {
        width: 100%;
      }
  </style>
</head>
<body>
  <header class="site-header" role="banner">
    <div class="wrapper">
      <a class="site-title">Little Delvings</a>
      <nav class="site-nav">
        <a class="page-link" href="https://search.digitaltolkien.com/">Search&nbsp;Tolkien</a>
        <a class="page-link" href="https://digitaltolkien.com/">Digital&nbsp;Tolkien&nbsp;Project</a>
      </nav>
    </div>
  </header>
  <main class="page-content">
    <div class="wrapper">
      <p>
        These are little visualizations based on the text and annotations of the Digital Tolkien Project.
        The code for each one is available as is the summary data where possible.
      </p>
      <p>
        They are also posted to <a href="https://www.instagram.com/digitaltolkien/">Instagram</a>
        and <a href="https://twitter.com/digitaltolkien">Twitter</a>.
      </p>
""")

for i in range(1, 12):
    image_path = f"{i:03d}/{i:03d}.png"
    code_path = f"https://github.com/digitaltolkien/little-delvings/tree/main/{i:03d}"
    meta_path = f"{i:03d}/meta.yaml"

    meta = yaml.safe_load(open(meta_path))

    image_path
    code_path
    number = meta["number"]
    title = meta["title"]
    description = meta["description"]
    description_html = description.replace("\n", "<br>")

    print(f"""
      <div class="delving">
        <img src="{image_path}">
        <h2>{number:03d}. {title}</h2>
        <div class="description">{description_html}</div>
        <div class="code"><a href="{code_path}">code</a><div>
      </div>
    """)

print("""
    </div>
  </main>
</body>
</html>
""")