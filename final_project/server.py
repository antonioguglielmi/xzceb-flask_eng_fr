

from flask import Flask, render_template, request
import json
import machinetranslation as mt


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated = mt.translator.englishToFrench(textToTranslate)
    return translated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated = mt.translator.frenchToEnglish(textToTranslate)
    return translated

@app.route("/")
def renderIndexPage():
    render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
