from flask import Flask, render_template, request,flash,url_for,redirect
app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def Inginput():
	return render_template("Inginput.html")



@app.route('/handle_data', methods = ['POST', 'GET'])
def handle_data():
	usertext = request.form['ingtext']
	ad=str(usertext)
	temp=str(func(ad)[0])
	temp2=str(func(ad)[1])
	return render_template('op.html',query=usertext,quant=temp,unit=temp2)


def func(text):
    import re
    import spacy
    nlp = spacy.load('en')
    text=re.sub( r'([0-9])([a-zA-Z])', r'\1 \2', text)
    text=re.sub(' +',' ',text)
    doc=nlp(text)
    
    for token in doc:
        if token.dep_ == 'nummod':
            quant=token.text
        for child in token.children:
            if str(child)==quant:
                return (quant,token.lemma_)

if __name__ == '__main__':
   app.run(debug = True)
