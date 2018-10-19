from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    USD = float(request.args['USD'])
    #The request object stores information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #The information in args is visable in the url for the page being requested. ex. .../response?color=orange

    reply = USD * 19.26
        
    return render_template('response.html',response='$' + str(reply))
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
