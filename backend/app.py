"""
Flask API server for the Periodic Table application.
Provides endpoints to retrieve element data.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from elements_data import ELEMENTS_DATA, ELEMENTS_BY_NUMBER, ELEMENTS_BY_SYMBOL, ELEMENT_CATEGORIES, PERIODIC_TABLE_LAYOUT

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/elements', methods=['GET'])
def get_all_elements():
    """Return all elements in the periodic table."""
    return jsonify({
        'elements': ELEMENTS_DATA,
        'categories': ELEMENT_CATEGORIES,
        'layout': PERIODIC_TABLE_LAYOUT
    })

@app.route('/api/elements/<identifier>', methods=['GET'])
def get_element(identifier):
    """
    Return a specific element by atomic number or symbol.
    
    Args:
        identifier: Either an atomic number (int) or element symbol (str)
    """
    # Try to parse as atomic number first
    try:
        atomic_number = int(identifier)
        if atomic_number in ELEMENTS_BY_NUMBER:
            return jsonify(ELEMENTS_BY_NUMBER[atomic_number])
        return jsonify({'error': f'Element with atomic number {atomic_number} not found'}), 404
    except ValueError:
        # If not a number, try as symbol
        symbol = identifier
        if symbol in ELEMENTS_BY_SYMBOL:
            return jsonify(ELEMENTS_BY_SYMBOL[symbol])
        return jsonify({'error': f'Element with symbol {symbol} not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
