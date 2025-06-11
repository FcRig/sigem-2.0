from flask import Blueprint, request, jsonify, abort
from .tasks import scrape_page

scraper_bp = Blueprint('scraper', __name__)


@scraper_bp.route('/', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        abort(400, description="url parameter required")
    result = scrape_page(url)
    return jsonify(result)
