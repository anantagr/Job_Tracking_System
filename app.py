from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        linkedin_job_title = request.form['linkedin_job_title']
        linkedin_job_location = request.form['linkedin_job_location']
        path = request.form['path']
        
        file_name = 'job_tracking_data - ' + linkedin_job_title + '.xlsx'
        
        from job_tracking_system import main
        result_string = main(linkedin_job_title, linkedin_job_location, file_name, path)
        
        return render_template('result.html', pythjon = linkedin_job_title, s1 = result_string[0], s2 = result_string[1], s3 = result_string[2])


if __name__=='__main__':
    app.debug = True
    app.run()