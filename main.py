#!/usr/bin/env python3
import os
from app import create_app
from config import Config


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()
