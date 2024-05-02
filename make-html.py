#!/usr/bin/env python3

import sys

index_header = """<html>
<head>
  <title>Digital Tolkien: Little Delvings</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="charset" content="utf-8">
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
      img {
        box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
        width: 100%;
      }
      figure {
        max-width: 960px;
        margin: 20px;
        display: flex; 
        flex-direction: column;
      }
      p {
        font-size: 18pt;
        font-weight: 300;
        line-height: 1.5;
        margin-block: 2em;
      }
  </style>
  <script defer data-domain="delvings.digitaltolkien.com" src="https://plausible.io/js/script.js"></script>
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
      </p>
"""

index_footer = """
    </div>
  </main>
</body>
</html>
"""


def make_index(latest):
    with open("index.html", "w") as f:
        f.write(index_header)

        for i in range(latest, 0, -1):
            alt = open(f"alt-text/{i:04d}.txt").read().strip()
            f.write(f"""<figure><img src="images/{i:04d}.png" alt="{alt}"></figure>\n""")

        f.write(index_footer)


def make_latest(latest):
    with open("latest.html", "w") as f:
        f.write('<body style="margin: 0;">\n')
        alt = open(f"alt-text/{latest:04d}.txt").read().strip()
        f.write(f'<img src="images/{latest:04d}.png" width="100%" alt="{alt}">\n')
        f.write('</body>\n')


latest = int(sys.argv[1])
make_index(latest)
make_latest(latest)

