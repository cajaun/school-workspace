# COMP1220 Site

This folder contains a static personal profile and favorites site.

## Runtime Shape

~~~text
index.html -> index.css
            -> index.js
            -> images/
~~~

The HTML page provides the structure, the stylesheet controls presentation, the JavaScript file handles page behavior, and the image directory stores local media used by the page.

## Local Preview

Open `index.html` in a browser, or serve the folder from the repository root:

~~~bash
python3 -m http.server 8000 --directory Html/COMP1220
~~~

Open `http://localhost:8000` after starting the server.

## Files

| File or folder | Role |
| --- | --- |
| `index.html` | Page structure and content |
| `index.css` | Site styling |
| `index.js` | Client-side interactions |
| `images/` | Local image assets |

The page also references external web resources. Browser checks should run with network access when those resources matter to the visual result.
