from run import app

@app.errorhandler(Exception)
def server_error(error):
    app.logger.exception(error)

    return    {
        "code": 500,
        "name": error.__class__.__name__,
        "description": str(error),
    }, 500