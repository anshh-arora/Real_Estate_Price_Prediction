from app import app


if __name__ == "__main__":
    print("Starting python flask server for Real estate price prediction")
    app.run(debug=True,host="0.0.0.0")