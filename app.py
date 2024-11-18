from flask import Flask, render_template, request, jsonify
import crime_analysis

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/states', methods=['GET'])
def get_states():
    try:
       
        states = crime_analysis.get_all_states()
        return jsonify(states)
    except Exception as e:
        print(f"Error retrieving states: {e}")
        return jsonify([])

@app.route('/index', methods=['GET', 'POST'])
def index():
    state = request.args.get('state', '').strip()

    if not state:
        return render_template('index.html')

    print(f"Fetching data for state: {state}")
    crime_data, graphs = crime_analysis.get_crime_data_for_state(state)

    if crime_data is None:
        return render_template('index.html', error="No data found for the selected state.")

    return render_template('index.html', crime_data=crime_data, graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)