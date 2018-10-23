from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    USD = float(request.args['USD'])
    reply = USD * 19.35
    return render_template('response.html',response='$' + str(reply))
    
@app.route("/page1")
def render_er():
    return render_template('page1.html')
    
@app.route("/response1")
def render_response():
    feet = float(request.args['feet'])
    reply = feet * 0.3048
    return render_template('response.html',str(reply))
   
@app.route("/page2")
def render_q():
    return render_template('page2.html')
    
@app.route("/response2")
def render_response():
    feet = float(request.args['pounds'])
    reply = pounds * 0.453592 
    return render_template('response.html',str(reply))

    
    #The request object stores information about the request sent to the server.
    #args is a MultiDict (like a dictionary but can have multiple values for the same key)
    #The information in args is visable in the url for the page being requested. ex. .../response?color=orange

 
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
