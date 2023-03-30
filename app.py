from flask import Flask,render_template,redirect,request,flash,redirect,url_for
import json
import os.path

app=Flask(__name__)
app.secret_key="my_secret_key"

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/url_short',methods=["GET","POST"])
def url_short():
    if request.method=="POST":
        urls={}
        sh_code=request.form["code"]
        if os.path.exists("urls.json"):
            with open('urls.json') as urls_file:
                urls=json.load(urls_file)
        
        if sh_code in urls.keys():
            flash('The short code you entered already taken.Please take another')
            return redirect(url_for('index'))
            
        urls[sh_code]={'url':request.form["url"]}
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
        return render_template("short_url.html",srt_code=sh_code,srt_url=request.form["url"])
    else:
        return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True,port=5003)
