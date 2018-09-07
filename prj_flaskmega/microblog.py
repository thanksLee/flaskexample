from app import app, db
from app.models import User, Post, Message, Notification

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post, "Message": Message, "Notification": Notification}



app.run(debug=True, port=4999)
#app.run(port=4999)