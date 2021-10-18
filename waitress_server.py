from waitress import serve
import __init__
serve(__init__.app, host='0.0.0.0', port=8080)