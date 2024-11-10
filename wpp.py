 # from flask import Flask,request,flash,render_template
# from flask_mail import Mail,Message

# app =Flask(__name__)
# app.secret_key="123"

# @app.route("/send_email",methods=["POST","GET"])
# def send_email():
#    if request.method=="POST":
#       fmail=request.form.get('fmail')
#       tmail = request.form.get('tmail')
#       fpwd = request.form.get('fpwd')
#       subject = request.form.get('subject')
#       message = request.form.get('message')

#       app.config['MAIL_SERVER']='smtp.gmail.com'
#       app.config['MAIL_PORT']=465
#       app.config['MAIL_USERNAME']=fmail
#       app.config['MAIL_PASSWORD']=fpwd
#       app.config['MAIL_USE_TLS']=False
#       app.config['MAIL_USE_SSL']=True

#       mail = Mail(app)

#       msg=Message(subject,sender=fmail,recipients=[tmail])
#       msg.body=message
#       mail.send(msg)
#       flash("Mail Sented Successfully", 'success')
#       return render_template('port.html')

# if __name__ == '__main__':
#    app.run(debug = True)







from flask import Flask, request, flash, render_template
from flask_mail import Mail, Message

wpp = Flask(__name__)
wpp.secret_key = "123"

@wpp.route("/", methods=["POST", "GET"])
def send_email():
    if request.method == "POST":
        fmail = request.form.get('fmail')
        tmail = request.form.get('tmail')
        fpwd = request.form.get('fpwd')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Configuration for Flask-Mail
        wpp.config['MAIL_SERVER'] = 'smtp.gmail.com'
        wpp.config['MAIL_PORT'] = 465
        wpp.config['MAIL_USERNAME'] = fmail
        wpp.config['MAIL_PASSWORD'] = fpwd
        wpp.config['MAIL_USE_TLS'] = False
        wpp.config['MAIL_USE_SSL'] = True

        mail = Mail(wpp)

        # Creating the email message
        msg = Message(subject, sender=fmail, recipients=[tmail])
        msg.body = message
        
        try:
            mail.send(msg)
            flash("Mail sent successfully!", 'success')
        except Exception as e:
            flash(f"An error occurred: {e}", 'error')

        return render_template('port.html')

    # Render form if GET request
    return render_template('port.html')

if __name__ == '__main__':
    wpp.run(debug=True)
