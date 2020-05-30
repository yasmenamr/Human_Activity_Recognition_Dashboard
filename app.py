import logging

from Human_Activity_Recognition import app

server = app.server

if __name__ == "__main__":
    logger = logging.getLogger('my-logger')
    logger.propagate = False
    app.run_server(debug=True)