# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - present Junior Bessong
"""

from api import app, db

@app.shell_context_processor
def make_shell_context():
    return {"app": app,
            "db": db
            }

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8000)
    