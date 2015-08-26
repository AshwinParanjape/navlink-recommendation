from flask import Flask, request, Response, jsonify, render_template
from navlinkRecommender import navlinkRecommender
from werkzeug.debug import DebuggedApplication
import json

app = Flask(__name__)
app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

recommenderObj = navlinkRecommender()


@app.route('/')
def home():
    return Response("""Navlink-recommendation Tool Usage\n * Top k -- /topk/<k>/\n * All recommendations for a source -- /<article>/\n * Top k recommendations for a source -- /<article>/<k>/\n""",  content_type='text/plain')

@app.route('/edit/<article>/')
def edit(article):
    return render_template('edit_test.html', article=article)

@app.route('/topk/<int:k>/')
def getTopK(k):
    return jsonify(recommendations = recommenderObj.getTopRecommendations(k))

@app.route('/<article>/')
def getSource(article):
    return jsonify(recommendations = recommenderObj.getRecommendationsForSource(article))

@app.route('/<article>/<int:k>/')
def getSourceTopK(article, k):
    return jsonify(recommendations = recommenderObj.getRecommendationsForSource(article,k))



if __name__ == '__main__':
    app.run(debug=True)
