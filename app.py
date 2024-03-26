from flask import Flask, render_template,request,redirect,url_for
l=[]
app=Flask(__name__)
@app.route('/')
def main_page():
    #return "Hello World!"
    return render_template('portfolio.html')
@app.route('/aboutme')
def about():
    return render_template('about.html')

@app.route('/projects')
def education():
    return render_template('education.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/ledger_add', methods=['GET', 'POST'])
def ledger_add():
    if request.method == 'POST':
        trip = {
            'place': request.form['place'],
            'trip_start_date': request.form['trip_start_date'],
            'trip_end_date': request.form['trip_end_date'],
            'places_visited': request.form['places_visited'],
            'total_cost': request.form['total_cost']
            }
        l.append(trip)  # Append to the "ledger" list
        # Redirect to ledger_view route after adding trip
        #return redirect(url_for('ledger_view'))
    return render_template('ledger_add.html')



@app.route('/ledger_view')
def ledger_view():
    return render_template('ledger_view.html', trips=l)  # Pass trips stored in the ledger list to the template

if __name__=="__main__":
    app.run(debug=True,port=7000)