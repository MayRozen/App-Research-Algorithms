# Running the server
# need to run in terminal: export FLASK_RUN_PORT=5123

import dotenv, os
dotenv.load_dotenv()  # load FLASK_RUN_PORT

from flaskApp import app
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("FLASK_RUN_PORT"), host='0.0.0.0')


    