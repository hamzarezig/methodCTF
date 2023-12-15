from flask import Flask, render_template, make_response, request

app = Flask(__name__)
PORT = 8080

@app.route('/', methods=['GET', 'BEST', 'OPTIONS'])
def handle_request():
    if request.method == 'BEST':
        return render_template('flag.html')
    elif request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Methods'] = 'GET, BEST, OPTIONS'
        return response, 200
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=PORT, debug=True)

