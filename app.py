from flask import Flask, render_template, request, redirect, url_for
import phonenumbers
from phonenumbers import geocoder, carrier

app = Flask(__name__)
     
@app.route('/')
@app.route('/trace', methods =['GET', 'POST'])
def trace():
    mesage = ''    
    phoneNumber = ''
    phoneDetails = ''
    serviceProvider = ''
    if request.method == 'POST' and 'number' in request.form:
        number = request.form['number']
        if not number:
            mesage = 'Please enter mobile number with country code!'
        else:
            phoneNumber = phonenumbers.parse(number)
            phoneDetails = geocoder.description_for_number(phoneNumber, 
                                          'en')
            serviceProvider = carrier.name_for_number(phoneNumber,
            
                                  'en')
    return render_template('trace.html', mesage = mesage, phoneNumber = phoneNumber, phoneDetails = phoneDetails, serviceProvider = serviceProvider)
    
if __name__ == "__main__":
    app.run()   