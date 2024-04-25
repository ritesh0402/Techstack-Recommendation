from flask import Flask, render_template, request

from main import suggest_tech_stack, min_max_scaling

app = Flask(__name__)


df = min_max_scaling()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    user_requirements = {
        'DeveloperExperienceRequired': float(request.form['dev_exp']),
        'ComplexityOfProject': float(request.form['complexity']),
        'ProjectScale': float(request.form['scale']),
        'PerformanceOfTechnology': float(request.form['performance']),
        'CommunitySupport': float(request.form['community']),
        'Scalability': float(request.form['scalability']),
        'SecurityFeatures': float(request.form['security']),
        'Cost': float(request.form['cost']),
        'IntegrationCapabilities': float(request.form['integration']),
        'DocumentationQuality': float(request.form['documentation']),
        'LearningCurve': float(request.form['learning']),
        'CommunityAdoption': float(request.form['adoption']),
        'PerformanceScaling': float(request.form['performance_scaling']),
        'VendorLockIn': float(request.form['vendor_lockin']),
        'EcosystemSupport': float(request.form['ecosystem']),
        'LongTermSupport': float(request.form['long_term'])
    }
    recommended_tech = suggest_tech_stack(df, user_requirements)

    return render_template('result.html', recommended_tech=recommended_tech)

if __name__ == '__main__':
    app.run(debug=True)
