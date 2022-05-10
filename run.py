from market import app


# checks if the run.py file has run direcly and not imported

if __name__ == '__main__': 
    app.run(debug=True)