from flask import Flask, request, jsonify
import output
app = Flask (__name__)

@app.route("/getResponse/")
def get_user():
    extra = request.args.get("name")
    out = output.resultGeneration(extra)
    user_data = {  "status" : "SUCCESS",
                    "response" : out
                 }

    return jsonify(user_data)

if __name__ == "__main__":
    app.run(debug=True)
