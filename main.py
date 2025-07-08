from flask import Flask, render_template, request, jsonify
import markdown


app = Flask(__name__)

@app.route("/markdown", methods=["GET", "POST"])
def markdown_path():
    if request.method == "POST":
        data = request.get_json()
        markdown_content = data.get("markdown", "")
        html_content = markdown.markdown(
            markdown_content,
            extensions=[
                "fenced_code",
                "codehilite",
                "tables",
                "nl2br",
                "sane_lists",
                "smarty",
                "attr_list",
            ],
            extension_configs={
                'codehilite': {
                    'linenums': False,
                    'guess_lang': True,
                    'noclasses': True,
                }
            }
        )
        return jsonify({"html": html_content})
    return render_template("markdown.html")


if __name__=="__main__":
    app.run()