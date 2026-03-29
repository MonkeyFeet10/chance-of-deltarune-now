from pathlib import Path
location = Path(__file__).resolve().parent.parent / "docs" / "index.html"
with open(location, 'r', encoding="utf-8") as file:
	html = file.read()
if "chance of deltarune now" in html.lower():
	print(f"File \"{location}\" is already patched. Exiting...")
	from sys import exit
	exit(0)
url_patch = "https://pygame-web.github.io/cdn/0.9.3//browserfs.min.js"
dialog_patch = """
	<!--
		Chance of Deltarune Now Patch (created by PROJECT_ROOT/src/patch.py)
		This patch prevents the "unsaved changes" dialog from appearing.
		A patch is also made above here to fix the browserfs URL.
	-->
	<script>
		window.addEventListener("load", () => {
    		window.onbeforeunload = null;
    		window.addEventListener("beforeunload", (e) => {
    		    e.stopImmediatePropagation();
    		}, true);
		});
	</script>
</body>
"""
html = html.replace("https://pygame-web.github.io/cdn/0.9.3//browserfs.min.js", url_patch)
html = html.replace("</body>", dialog_patch)
with open(location, 'w', encoding="utf-8") as file:
	file.write(html)
print(f"File \"{location}\" patched.")