from flask import Flask


app = Flask(__name__)
config_filename = "config"
app.config.from_object(config_filename)

from app import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

@app.errorhandler(404)
def page_not_found(e):
    return {"message": "not found", "error": "404", "api":"/api/gravatars"}, 404
app.run(debug=True)




