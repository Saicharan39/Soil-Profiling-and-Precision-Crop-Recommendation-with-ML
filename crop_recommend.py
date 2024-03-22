
# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# import pickle
# import cx_Oracle

# app = Flask(__name__)

# # Load the model
# loaded_model = pickle.load(open('crop.pkl', 'rb'))

# # Crop dictionary
# crop_dict = {
#     "rice": 1, "maize": 2, "jute": 3, "cotton": 4, "coconut": 5, "papaya": 6, "orange": 7,
#     "apple": 8, "muskmelon": 9, "watermelon": 10, "grapes": 11, "mango": 12, "banana": 13,
#     "pomegranate": 14, "lentil": 15, "blackgram": 16, "mungbean": 17, "mothbeans": 18,
#     "pigeonpeas": 19, "kidneybeans": 20, "chickpea": 21, "coffee": 22
# }

# # Oracle Database connection
# dsn_tns = cx_Oracle.makedsn('DESKTOP-JRAAC71', 1521, service_name='XE')
# db_connection = cx_Oracle.connect(user='system', password='saicharan', dsn=dsn_tns)
# cursor = db_connection.cursor()

# # User input for prediction
# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=['POST'])
# def predict():
#     # Extracting features from the form
#     N = int(request.form['Nitrogen'])
#     P = int(request.form['Phosphorus'])
#     K = int(request.form['Potassium'])
#     temp = float(request.form['Temperature'])
#     humidity = float(request.form['Humidity'])
#     ph = float(request.form['pH'])
#     rainfall = float(request.form['Rainfall'])
#     soil = request.form['Soil']

#     # Creating a DataFrame with the input features
#     input_df = pd.DataFrame({'N': [N], 'P': [P], 'K': [K], 'temperature': [temp],
#                              'humidity': [humidity], 'ph': [ph], 'rainfall': [rainfall], 'soil': [soil]})

#     # Validation for pH, temperature, humidity, and soil
#     ph_value = float(input_df['ph'].values[0])
#     temp_value = float(input_df['temperature'].values[0])
#     humidity_value = float(input_df['humidity'].values[0])
#     soil_value = input_df['soil'].values[0]

#     print("Input values:", N, P, K, temp, humidity, ph, rainfall, soil)
#     print("pH:", ph_value, "Temperature:", temp_value, "Humidity:", humidity_value, "Soil:", soil_value)

#     if 0 < ph_value <= 14 and 0 < temp_value < 60 and humidity_value > 0 and soil_value in ["Alluvial", "Black", "Clay", "Red"]:
#         # One-hot encoding for the "soil" attribute
#         input_df['soil'] = input_df['soil'].map({'Alluvial': 0, 'Black': 1, 'Clay': 2, 'Red': 3})

#         # Ensure that the input data columns match the expected columns used during training
#         expected_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'soil']
#         input_df = input_df.reindex(columns=expected_columns, fill_value=0)

#         # Make predictions using the loaded model
#         result = loaded_model.predict(input_df)

#         print("Prediction result:", result)

#         # Handling prediction result
#         predicted_crop_id = result[0]
#         if predicted_crop_id in crop_dict:
#             print("Crop is present in dictionary.")
#             crop = predicted_crop_id
#             result_str = "{} is the suitable crop ".format(crop)

#             # Insert runtime values into Oracle Database
#             insert_query = "INSERT INTO prediction (N, P, K, temperature, humidity, ph, rainfall, soil, predicted_crop) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
#             cursor.execute(insert_query, (N, P, K, temp, humidity, ph, rainfall, soil, crop))
#             db_connection.commit()

#             return render_template('index.html', result=str(result_str))
#         else:
#             print("Crop not found in dictionary.")
#             print("Crop from result:", repr(predicted_crop_id))
#             print("Crop dictionary keys:", crop_dict.keys())
#             return "Sorry, we could not determine the best crop to be cultivated with the provided data."
#     else:
#         return "Sorry... Error in entered values in the form. Please check the values and fill it again."

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #######################################################################################################################################
    
# from flask import Flask, render_template, redirect, url_for
# import cx_Oracle
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import InputRequired, Length
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# import numpy as np
# import pandas as pd
# import pickle


# app = Flask(__name__)
# app.secret_key = 'its_a_secret'

# # Load the model
# loaded_model = pickle.load(open('crop.pkl', 'rb'))

# # Crop dictionary
# crop_dict = {
#     "rice": 1, "maize": 2, "jute": 3, "cotton": 4, "coconut": 5, "papaya": 6, "orange": 7,
#     "apple": 8, "muskmelon": 9, "watermelon": 10, "grapes": 11, "mango": 12, "banana": 13,
#     "pomegranate": 14, "lentil": 15, "blackgram": 16, "mungbean": 17, "mothbeans": 18,
#     "pigeonpeas": 19, "kidneybeans": 20, "chickpea": 21, "coffee": 22
# }

# # Oracle Database connection
# dsn_tns = cx_Oracle.makedsn('DESKTOP-JRAAC71', 1521, service_name='XE')
# db_connection = cx_Oracle.connect(user='system', password='saicharan', dsn=dsn_tns)
# cursor = db_connection.cursor()

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


# class User(UserMixin):
#     def __init__(self, name, mobile_number):
#         self.name = name
#         self.mobile_number = mobile_number

#     def get_id(self):
#         return str(self.name)

# @login_manager.user_loader
# def load_user(user_name):
#     query = "SELECT name, mobile_number FROM users WHERE name = :1"
#     cursor.execute(query, (user_name,))
#     result = cursor.fetchone()
#     if result:
#         return User(result[0], result[1])
#     return None

# class LoginForm(FlaskForm):
#     name = StringField('Name', validators=[InputRequired(), Length(min=4, max=20)])
#     mobile_number = StringField('Mobile Number', validators=[InputRequired(), Length(min=10, max=255)])
#     submit = SubmitField('Login')


# class RegisterForm(FlaskForm):
#     name = StringField('Name', validators=[InputRequired(), Length(min=2, max=50)])
#     mobile_number = StringField('Mobile Number', validators=[InputRequired(), Length(min=10, max=255)])
#     submit = SubmitField('Register')


# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         query = "SELECT name, mobile_number FROM users WHERE name = :1"
#         cursor.execute(query, (form.name.data,))
#         result = cursor.fetchone()
#         if result and result[1] == form.mobile_number.data:
#             user = User(result[0], result[1])
#             login_user(user)
#             print("Login successful!")
#             return redirect(url_for('index'))
#         else:
#             print("Incorrect credentials!")
#     return render_template('login.html', form=form)

# @app.route('/index', methods=['GET', 'POST'])
# @login_required
# def dashboard():
#     return render_template('index.html', name=current_user.name)

# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         insert_query = "INSERT INTO users(name, mobile_number) VALUES (:1, :2)"
#         cursor.execute(insert_query, (form.name.data, form.mobile_number.data))
#         db_connection.commit()
#         return redirect(url_for('login'))
    
#     return render_template('register.html', form=form)




# @app.route("/predict", methods=['POST'])
# def predict():
#     # Extracting features from the form
#     N = int(request.form['Nitrogen'])
#     P = int(request.form['Phosphorus'])
#     K = int(request.form['Potassium'])
#     temp = float(request.form['Temperature'])
#     humidity = float(request.form['Humidity'])
#     ph = float(request.form['pH'])
#     rainfall = float(request.form['Rainfall'])
#     soil = request.form['Soil']

#     # Creating a DataFrame with the input features
#     input_df = pd.DataFrame({'N': [N], 'P': [P], 'K': [K], 'temperature': [temp],
#                              'humidity': [humidity], 'ph': [ph], 'rainfall': [rainfall], 'soil': [soil]})

#     # Validation for pH, temperature, humidity, and soil
#     ph_value = float(input_df['ph'].values[0])
#     temp_value = float(input_df['temperature'].values[0])
#     humidity_value = float(input_df['humidity'].values[0])
#     soil_value = input_df['soil'].values[0]

#     print("Input values:", N, P, K, temp, humidity, ph, rainfall, soil)
#     print("pH:", ph_value, "Temperature:", temp_value, "Humidity:", humidity_value, "Soil:", soil_value)

#     if 0 < ph_value <= 14 and 0 < temp_value < 60 and humidity_value > 0 and soil_value in ["Alluvial", "Black", "Clay", "Red"]:
#         # One-hot encoding for the "soil" attribute
#         input_df['soil'] = input_df['soil'].map({'Alluvial': 0, 'Black': 1, 'Clay': 2, 'Red': 3})

#         # Ensure that the input data columns match the expected columns used during training
#         expected_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'soil']
#         input_df = input_df.reindex(columns=expected_columns, fill_value=0)

#         # Make predictions using the loaded model
#         result = loaded_model.predict(input_df)

#         print("Prediction result:", result)

#         # Handling prediction result
#         predicted_crop_id = result[0]
#         if predicted_crop_id in crop_dict:
#             print("Crop is present in dictionary.")
#             crop = predicted_crop_id
#             result_str = "{} is the suitable crop ".format(crop)

#             # Insert runtime values into Oracle Database
#             insert_query = "INSERT INTO prediction (name,mobile_number,N, P, K, temperature, humidity, ph, rainfall, soil, predicted_crop) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
#             cursor.execute(insert_query, (name,mobile_number,N, P, K, temp, humidity, ph, rainfall, soil, crop))
#             db_connection.commit()

#             return render_template('index.html', result=str(result_str))
#         else:
#             print("Crop not found in dictionary.")
#             print("Crop from result:", repr(predicted_crop_id))
#             print("Crop dictionary keys:", crop_dict.keys())
#             return "Sorry, we could not determine the best crop to be cultivated with the provided data."
#     else:
#         return "Sorry... Error in entered values in the form. Please check the values and fill it again."

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
#########################################################################################################################################











from flask import Flask, render_template, redirect, url_for, request
import cx_Oracle
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = 'its_a_secret'

# Load the model
loaded_model = pickle.load(open('crop.pkl', 'rb'))

# Crop dictionary
crop_dict = {
    "rice": 1, "maize": 2, "jute": 3, "cotton": 4, "coconut": 5, "papaya": 6, "orange": 7,
    "apple": 8, "muskmelon": 9, "watermelon": 10, "grapes": 11, "mango": 12, "banana": 13,
    "pomegranate": 14, "lentil": 15, "blackgram": 16, "mungbean": 17, "mothbeans": 18,
    "pigeonpeas": 19, "kidneybeans": 20, "chickpea": 21, "coffee": 22
}

# Oracle Database connection
dsn_tns = cx_Oracle.makedsn('DESKTOP-JRAAC71', 1521, service_name='XE')
db_connection = cx_Oracle.connect(user='system', password='saicharan', dsn=dsn_tns)
cursor = db_connection.cursor()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, name, mobile_number):
        self.name = name
        self.mobile_number = mobile_number

    def get_id(self):
        return str(self.name)

@login_manager.user_loader
def load_user(user_name):
    query = "SELECT name, mobile_number FROM users WHERE name = :1"
    cursor.execute(query, (user_name,))
    result = cursor.fetchone()
    if result:
        return User(result[0], result[1])
    return None

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=20)])
    mobile_number = StringField('Mobile Number', validators=[InputRequired(), Length(min=10, max=255)])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=50)])
    mobile_number = StringField('Mobile Number', validators=[InputRequired(), Length(min=10, max=255)])
    submit = SubmitField('Register')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        query = "SELECT name, mobile_number FROM users WHERE name = :1"
        cursor.execute(query, (form.name.data,))
        result = cursor.fetchone()
        if result and result[1] == form.mobile_number.data:
            user = User(result[0], result[1])
            login_user(user)
            print("Login successful!")
            return redirect(url_for('dashboard'))
        else:
            print("Incorrect credentials!")
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('index.html', name=current_user.name)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        insert_query = "INSERT INTO users(name, mobile_number) VALUES (:1, :2)"
        cursor.execute(insert_query, (form.name.data, form.mobile_number.data))
        db_connection.commit()
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route("/predict", methods=['POST'])
def predict():
    # Extracting features from the form
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorus'])
    K = int(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['pH'])
    rainfall = float(request.form['Rainfall'])
    soil = request.form['Soil']

    # Creating a DataFrame with the input features
    input_df = pd.DataFrame({'N': [N], 'P': [P], 'K': [K], 'temperature': [temp],
                             'humidity': [humidity], 'ph': [ph], 'rainfall': [rainfall], 'soil': [soil]})

    # Validation for pH, temperature, humidity, and soil
    ph_value = float(input_df['ph'].values[0])
    temp_value = float(input_df['temperature'].values[0])
    humidity_value = float(input_df['humidity'].values[0])
    soil_value = input_df['soil'].values[0]

    print("Input values:", N, P, K, temp, humidity, ph, rainfall, soil)
    print("pH:", ph_value, "Temperature:", temp_value, "Humidity:", humidity_value, "Soil:", soil_value)

    if 0 < ph_value <= 14 and 0 < temp_value < 60 and humidity_value > 0 and soil_value in ["Alluvial", "Black", "Clay", "Red"]:
        # One-hot encoding for the "soil" attribute
        input_df['soil'] = input_df['soil'].map({'Alluvial': 0, 'Black': 1, 'Clay': 2, 'Red': 3})

        # Ensure that the input data columns match the expected columns used during training
        expected_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'soil']
        input_df = input_df.reindex(columns=expected_columns, fill_value=0)

        # Make predictions using the loaded model
        result = loaded_model.predict(input_df)

        print("Prediction result:", result)

        # Handling prediction result
        predicted_crop_id = result[0]
        if predicted_crop_id in crop_dict:
            print("Crop is present in dictionary.")
            crop = predicted_crop_id
            result_str = "{} is the suitable crop ".format(crop)

            # Insert runtime values into Oracle Database
            insert_query = "INSERT INTO prediction (name, mobile_number, N, P, K, temperature, humidity, ph, rainfall, soil, predicted_crop) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
            cursor.execute(insert_query, (current_user.name, current_user.mobile_number, N, P, K, temp, humidity, ph, rainfall, soil, crop))
            db_connection.commit()

            return render_template('index.html', result=str(result_str))
        else:
            print("Crop not found in dictionary.")
            print("Crop from result:", repr(predicted_crop_id))
            print("Crop dictionary keys:", crop_dict.keys())
            return "Sorry, we could not determine the best crop to be cultivated with the provided data."
    else:
        return "Sorry... Error in entered values in the form. Please check the values and fill it again."

if __name__ == '__main__':
    app.run(debug=True)

