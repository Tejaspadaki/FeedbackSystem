from flask import Flask, redirect, render_template, request, session, url_for, flash, jsonify
from flask_mysqldb import MySQL
import MySQLdb
import requests
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'SGUCQ@ERP143'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)


# Database configuration
app.config['MYSQL_HOST'] = 'erp-sgu.cnw0ui8sevxl.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'SGUFeedback143'
app.config['MYSQL_DB'] = 'erpSGUDB'

mysql = MySQL(app)

#all API's
student_login_api = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/student_login"
hod_login_api = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/hod_login"
teacher_login_api = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/teacher_login"
fetch_subject_code = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/subject-code"
fetch_teacher_id = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/teacher-id"
fetch_student_profile = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/fetch_student_profile"
edit_profile = "https://cmadner97k.execute-api.ap-south-1.amazonaws.com/student_update_profile"
feedback_submit = 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/feedback_submit'

def sub_api(self, class_name):
        if class_name == 'TY A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/TY_A'
        elif class_name =='TY B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/TY_B'
        elif class_name =='TY C':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/TY_C'
        elif class_name =='SY A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/SY_A'
        elif class_name =='SY B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/SY_B'
        elif class_name =='SY C':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/SY_C'
        elif class_name =='Btech A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/CSE_BTech-A'
        elif class_name =='Btech B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/CSE_BTech-B'
        elif class_name=='FY A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/FY_A'
        elif class_name=='FY B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/FY_B'
        elif class_name=='FY C':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/FY_C'
        else:
            return 'No class'
#Classes
class Questions:
    option = -1

    def selected_option(self, option):
        if option == 'A':
            return 10
        elif option == 'B':
            return 7
        elif option == 'C':
            return 4
        elif option == 'D':
            return 2
        
    def class_name(self, cn):
        if cn == 'FY A':
            return 'FY_A'
        elif cn == 'FY B':
            return 'FY_B'
        elif cn == 'FY C':
            return 'FY_C'
        elif cn == 'SY A':
            return 'SY_A'
        elif cn == 'SY B':
            return 'SY_B'
        elif cn == 'SY C':
            return 'SY_C'
        elif cn == 'TY A':
            return 'TY_A'
        elif cn == 'TY B':
            return 'TY_B'
        elif cn == 'TY C':
            return 'TY_C'
        elif cn == 'Btech A':
            return 'Btech_A'
        elif cn == 'Btech B':
            return 'Btech_B'
        elif cn == 'FY A':
            return 'FY_A'
        elif cn == 'FY B':
            return 'FY_B'
        elif cn == 'FY C':
            return 'FY_C'

    def sub_api(self, class_name):
        if class_name == 'TY A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/TY_A'
        elif class_name =='TY B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/TY_B'
        elif class_name =='TY C':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/TY_C'
        elif class_name =='SY A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/SY_A'
        elif class_name =='SY B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/SY_B'
        elif class_name =='SY C':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/SY_C'
        elif class_name =='Btech A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/CSE_BTech-A'
        elif class_name =='Btech B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/CSE_BTech-B'
        elif class_name=='FY A':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/FY_A'
        elif class_name=='FY B':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/FY_B'
        elif class_name=='FY C':
            return 'https://cmadner97k.execute-api.ap-south-1.amazonaws.com/FY_C'
        else:
            return 'No class'


#landing page
@app.route('/')
def home():
    return render_template('landing-page.html')

#hod login
@app.route('/hod-login')
def hodlogin():
    return render_template('hod-login.html')

#teacher login
@app.route('/teacher-login')
def teacherlogin():
    return render_template('teacher-login.html')

#student login
@app.route('/student-login')
def login():
    return render_template('student-login.html')

#hod dashboard
@app.route('/hod-dashboard')
def hoddashboard():
    try:
        if 'email' in session:
            return render_template('HODDashboard.html')
        else:
            flash('Not login. Please first login to proceed')
            return redirect(url_for('hod_login'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.')
        return redirect(url_for('hod_login'))

#teacher dashboard
@app.route('/teacher-dashboard')
def teacherdashboard():
    try:
        # Check if 'email' is in session
        if 'email' in session:
            app.logger.info(f"User {session['email']} accessing dashboard")  # Log the session
            return render_template('teacher-dashboard.html')  # Render the actual dashboard template
        else:
            flash('You need to log in first to access the dashboard.')
            return redirect(url_for('teacher_login'))
    except KeyError as e:
        app.logger.error(f"Session key error: {e}")
        flash('Session expired. Please log in again.')
        return redirect(url_for('teacher_login'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.')
        return redirect(url_for('teacher_login'))


#student dashboard
@app.route('/student-dashboard')
def studentdashboard():
    try:
        if 'email' in session:
            return render_template('student-dashboard.html')
        else:
            flash('Your session has expired. Please log in again.')
            return redirect(url_for('login'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.')
        return redirect(url_for('login'))

# This below code is responsible for processing the login and displaying the dashboard for student, teacher, and HOD.

#for HOD
@app.route('/hod_login')
def hod_login():
    try:
        email = request.args.get('email')
        password = request.args.get('password')
        response = requests.get(hod_login_api, params={'hod_username': email, 'hod_password': password})
        response_data = response.json()

        if response_data.get('status') == 'success':
            session['email'] = email
            return redirect(url_for('hoddashboard'))
        else:
            flash('Invalid credentials. Please contact the admin.')
            return redirect(url_for('hodlogin'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.')
        return redirect(url_for('hodlogin'))
    
#for teacher
@app.route('/teacher-login', methods=['GET', 'POST'])
def teacher_login():
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            response = requests.get(teacher_login_api, params={'teacher_user_id': email, 'teacher_password': password})
            response_data = response.json()

            if response_data.get('status') == 'success':
                session['email'] = email
                session['name'] = response_data.get('teacher_name')
                return redirect(url_for('teacherdashboard'))
            else:
                flash('Invalid credentials. Please contact the admin.')
                return redirect(url_for('teacher_login'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.')
        return redirect(url_for('teacher_login'))

#for student
@app.route('/login')
def student_login():
    try:
        email = request.args.get('email')
        password = request.args.get('password')
        response = requests.get(student_login_api, params={'student_prn': email, 'student_password': password})
        response_data = response.json()

        if response_data.get('status') == 'success':
            session.permanent = True
            session['email'] = email
            session['name'] = response_data.get('student_name')
            session['attendance'] = response_data.get('student_attendance')
            session['year_class'] = response_data.get('student_year')
            return redirect(url_for('studentdashboard'))
        else:
            flash('Invalid credentials. Please contact the admin.')
            return redirect(url_for('login'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.')
        return redirect(url_for('login'))


#HOD profile
@app.route('/hod-profile')
def hodprofile():
    return render_template('hodprofile.html')

#techerprofile
@app.route('/teacher-profile')
def teacherprofile():
    return render_template('teacherprofile.html')

#Studentprofile
@app.route('/profile')
def profile():
    try:
        if 'email' in session:
            params = {'email': session['email']}
            
            # Debug: Print the URL and params being sent
            app.logger.info(f"API URL: {fetch_student_profile}")
            app.logger.info(f"Request Params: {params}")
            
            response = requests.get(fetch_student_profile, params=params)
            
            # Check for response status code
            if response.status_code == 200:
                try:
                    student_profile = response.json()
                    if student_profile.get('data'):
                        return render_template('StudentProfile.html', profile=student_profile['data'])
                    else:
                        flash('No profile data found.', 'warning')
                        return redirect(url_for('studentdashboard'))
                except ValueError as e:
                    app.logger.error(f"Failed to parse JSON: {e}")
                    flash('Failed to load profile data.', 'danger')
                    return redirect(url_for('studentdashboard'))
            else:
                # Debug: Log the response status code and content
                app.logger.error(f"API call failed with status code {response.status_code}. Response content: {response.content}")
                flash(f"API call failed with status code {response.status_code}.", 'danger')
                return redirect(url_for('studentdashboard'))
        else:
            flash('Not logged in. Please log in first.', 'danger')
            return redirect(url_for('login'))

    except Exception as e:
        app.logger.error(f"Error occurred while fetching profile: {e}")
        flash('An unexpected error occurred.', 'danger')
        return redirect(url_for('login'))
    
#HOD feedback report
@app.route('/hod-feedback-report', methods=['GET', 'POST'])
def hodfeedbackreport():
    try:
        if session.get('email'): 
            q = Questions()
            data = [
                {'class_name': 'Select Class'}, {'class_name': 'SY A'}, {'class_name': 'SY B'},
                {'class_name': 'SY C'}, {'class_name': 'TY A'}, {'class_name': 'TY B'},
                {'class_name': 'TY C'}, {'class_name': 'Btech A'}, {'class_name': 'Btech B'}
            ]
            sub_data = []
            selected_class = ''
            selected_subject = ''
            selected_teacher = ''
            pie_data = {}
            feedback_data = (('Q1', 0.0, 0.0, 0.0, 0.0, 0.0), ('Q2', 0.0, 0.0, 0.0, 0.0, 0.0), 
                             ('Q3', 0.0, 0.0, 0.0, 0.0, 0.0), ('Q4', 0.0, 0.0, 0.0, 0.0, 0.0), 
                             ('Q5', 0.0, 0.0, 0.0, 0.0, 0.0), ('Q6', 0.0, 0.0, 0.0, 0.0, 0.0), 
                             ('Q7', 0.0, 0.0, 0.0, 0.0, 0.0), ('Q8', 0.0, 0.0, 0.0, 0.0, 0.0), 
                             ('Q9', 0.0, 0.0, 0.0, 0.0, 0.0), ('Q10', 0.0, 0.0, 0.0, 0.0, 0.0), 
                             ('Average', 0.0, 0.0, 0.0, 0.0, 0.0))
            if request.method == 'POST':
                selected_class = request.form.get('selected_class')
                selected_subject = request.form.get('selected_subject')
                selected_teacher = request.form.get('selected_teacher')
                
                class_api = q.sub_api(selected_class)
                if class_api != 'No class':
                    response = requests.get(class_api)
                    response_data = response.json()
                    sub_data = response_data.get('data')

                if selected_subject != 'Select Subject' and selected_teacher != 'Select Teacher':
                    selected_yc = q.class_name(selected_class)

                    response = requests.get(fetch_teacher_id, params={'teacher_name': selected_teacher})
                    response_data = response.json()
                    selected_id = response_data.get('teacher_id')

                    response = requests.get(fetch_subject_code, params={'subject_name': selected_subject})
                    response_data = response.json()
                    selected_subject = response_data.get('subject_code')
                    
                    table_name = f"{selected_yc}_{selected_subject}_{selected_id}"
                    cur = mysql.connection.cursor()
                    cur.execute(f"SELECT * from {table_name}")
                    feedback_data = cur.fetchall()
                    
                    pie_data = {
                        "xValues": ["A", "B", "C", "D"],
                        "yValues": [feedback_data[10][1], feedback_data[10][2], feedback_data[10][3], feedback_data[10][4]]
                    }

            return render_template('hod-feedback-report.html', class_data=data, sub_data=sub_data, 
                                   selected_class=selected_class, feedback_data=feedback_data, 
                                   selected_subject=selected_subject, selected_teacher=selected_teacher, 
                                   pie_data=pie_data)
        else:
            flash('Not logged in. Please log in to proceed.')
            return redirect(url_for('hodLogin'))

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please select the correct Subject and Teacher.')
        return redirect(url_for('hodfeedbackreport'))

#studentfeedback
@app.route('/student-feedback')
def studentfeedback():
    try:
        if session.get('email'):
            response = requests.get(student_login_api, params={'student_prn': session['email'], 'student_password': session['email']})
            response_data = response.json()

            class_name = response_data.get('student_year')
            attendance = int(response_data.get('student_attendance'))
            
            if attendance >= 60:
                q = Questions()
                class_api = q.sub_api(class_name)
                response = requests.get(class_api)
                response_data = response.json()
                data = response_data.get('data')
                return render_template('student-feedback.html', data=data)
            else:
                flash('You cannot access the feedback section as your attendance is below 60%.', 'error')
                return redirect('/student-dashboard')
        else:
            flash('Not logged in. Please log in to proceed.', 'error')
            return redirect(url_for('login'))
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash('An unexpected error occurred. Please try again later.', 'error')
        return redirect(url_for('login'))
 
#editprofile
@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile_route():
    if 'email' not in session:
        flash('Please log in to edit your profile.', 'danger')
        return redirect(url_for('login'))

    try:
        if request.method == 'GET':
            response = requests.get(fetch_student_profile, params={'email': session['email']})
            student_profile = response.json()
            app.logger.info(f"Fetched Profile: {student_profile}")

            if student_profile.get('data'):
                return render_template('edit-profile.html', student_profile=student_profile.get('data'))
            else:
                flash('No profile found. Please create your profile.', 'warning')
                return redirect(url_for('profile')) 

        elif request.method == 'POST':

            updated_profile = {
                'PRN': request.form.get('PRN'),
                'Student_Year': request.form.get('Student_Year'),
                'Division': request.form.get('Division'),
                'Batch': request.form.get('Batch'),
                'Mobile': request.form.get('Mobile'),
                'Email': request.form.get('Email'),
                'DOB': request.form.get('DOB'),
                'Gender': request.form.get('Gender'),
                'Blood_group': request.form.get('Blood_group'),
                'Address': request.form.get('Address'),
                'Father_Name': request.form.get('Father_Name'),
                'Father_Mobile': request.form.get('Father_Mobile'),
                'Mother_Name': request.form.get('Mother_Name'),
                'Mother_Mobile': request.form.get('Mother_Mobile'),
                'Guardian_Name': request.form.get('Guardian_Name'),
                'Guardian_Mobile': request.form.get('Guardian_Mobile'),
                '10th_School_Name': request.form.get('10th_School_Name'),
                '10th_Marks': request.form.get('10th_Marks'),
                '12th_School_Name': request.form.get('12th_School_Name'),
                '12th_Marks': request.form.get('12th_Marks')
            }

            response = requests.get(edit_profile, params=updated_profile)
            response_data = response.json()

            if response_data.get('status') == 'success':
                flash("Profile successfully updated!", "success")
                # Redirect to the profile page after successful update
                return redirect(url_for('profile'))  # Assuming you have a profile_route
            else:
                flash(response_data.get('message', "Failed to update profile. Please try again."), "danger")

            return redirect(url_for('edit_profile_route'))

    except Exception as e:
        app.logger.error(f"Error occurred while editing profile: {e}", exc_info=True)
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(url_for('edit_profile_route'))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    try:
        student_prn = session.get('email') 
        selected_yc = session.get('year_class')
        selected_sub = request.form.get('subject_name')
        selected_teacher = request.form.get('teacher_name')

        if not student_prn or not selected_yc or not selected_sub or not selected_teacher:
            flash('Missing essential data. Please fill all fields.')
            return redirect(url_for('studentfeedback'))

        q = []

        for i in range(1, 11):
            selected_op = request.form.get(str(i))

            if not selected_op:
                flash(f'Missing option for question {i}')
                return redirect(url_for('studentfeedback'))

            q.append(selected_op)

        response = requests.get(feedback_submit, params={'student_prn': student_prn, 'year_class': selected_yc, 'subject_name': selected_sub, 'teacher_name': selected_teacher, 1: q[0], 2: q[1], 3: q[2], 4: q[3], 5: q[4], 6: q[5], 7: q[6], 8: q[7], 9: q[8], 10: q[9]})
        response_data = response.json()
        
        if response_data.get('status') == 'success':
            return render_template('feedbacksubmit.html')
        else:
            flash('Your feedback was not submitted')
            return redirect(url_for('studentfeedback'))

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        flash(' Please select the correct Subject and Teacher.')
        return redirect(url_for('studentfeedback'))

#logout
@app.route('/logout')
def logout():
    if session['email']:
        session.pop('email', None)
        return redirect('/')