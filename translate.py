from flask import Flask
import json
import requests
import googletrans as gt

## Creating our app instance
app = Flask(__name__)
serviceUrls = ['translate.google.com','translate.goole.co.kr']
translator = gt.Translator(serviceUrls)


@app.route("/translate/<text>/from/<source>/<dest>")
def translate(text,source,dest):
	return getTranslation(text, source, dest)


def getTranslation(text,source,dest):
	try:
		result = translator.translate(text,dest,source)
		print(result)
		return json.dumps({"text": result.text, "src": result.src, "dest": result.dest},ensure_ascii=False)
	except Exception as e:
		print(e)
		return str(e)


if __name__ == "__main__":
	app.run()

