from contextlib import redirect_stderr
from flask import Flask, render_template, request,jsonify
from werkzeug.utils import secure_filename
import socket
import pandas as pd

import os
df=pd.read_csv('login_cread.csv')
#cd={'UserName':object,'passwd':object}
#df=df.astype(cd)
print(df,df.dtypes)
if ((df['UserName']=='psk') & (df['passwd']==int('123'))[0]).bool():
          print('login successful')
host = socket.gethostname()
hip=socket.gethostbyname(host)
print(hip)
app = Flask(__name__)
##UPLOAD_FOLDER='./uploads'
##app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

##app.config['/uploads']
##app.config['']
###if file have containt text and and also that not related
#to any other software that cannot be access to that is the problem and
#i dont know
##what to do next i am stuck in the adding image in html file if that file text then txt png and if that file is  png or jpeg it means all
##that file containg image ext that will show the img.png icon and if file mp3 then it mp3 icon or if video then video icon that all

@app.route('/')
def index():
   return render_template("login.html",)

##@app.context_processor
##def utility_processor():
##   def f_ext(a):
##       if '.jpg' in file_ext or '.jpeg' in file_ext or '.png' in file_ext or '.bit' in file_ext:
##          print("hello:")
##          return 'img'
##func_dict = {
##    
##    "f_ext": f_ext
##            }

@app.route('/upload')
def upload():
    return render_template("upload.html")
   
	
@app.route('/upload', methods = ['GET', 'POST'])



def upload_file():
   if request.method == 'POST':
##      f = request.files['file']
##      f.save(secure_filename(f.filename))
##      return 'file uploaded successfully'
        filesDict = request.files.to_dict()
        # print('Forms:::', formDict)
        # print('files:::', filesDict)
        uploadData=request.files['media']
        data_file_name = uploadData.filename
        # print('data_file_name:::', data_file_name)
        # print(os.path.joi
        uploadData.save(os.path.join(app.root_path,'static\\upload\\'+data_file_name))
        msg  = 'File successfully uploaded ' + data_file_name + ' to the database!'
        
       # return jsonify({'htmlresponse': render_template('response.html', msg=msg)})
   return render_template('upload.html',msg=msg)

@app.route('/download',methods=['GET','POST'])

def download():
   try:
      if request.method=='POST':
           uname=request.form['uname']
           passwd=request.form['passwd']
           print('p')
           if ((df['UserName']==uname) & (df['passwd']==passwd)[0]).bool():
             print('login successful')
             files= os.listdir('./static/upload/Posters')
             return render_template('download.html',files=files,uname=uname)
   except TypeError:
      return render_template('login.html',files=files)
      

@app.route('/tutorial',methods=['GET','POST'])

def tutorial():
    
    return render_template('Tutorial.html',files=files)

@app.route('/login',methods=['GET','POST'])

def login():
   
##   form = LoginForm()
##   if form.validate_on_submit():
##      user = User.query.filter_by(email=form.email.data).first()
##      if user is not None and user.verify_password(form.password.data):
##         login_user(user, form.remember_me.data)
##         return redirect(request.args.get('next') or url_for('main.index'))
##      flash('Invalid username or password.')
##   return render_template('login.html', form=form)
            return render_template('login.html')

@app.route('/mainp')
def mainp():
   return render_template("mainpage.html",)
   
hs='192.168.43.31'
shs='192.168.229.1'



if __name__=='__main__':
    app.run(debug=False,host=shs,port=5123)
    
