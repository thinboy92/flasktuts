from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'Please enter your god name': 'Hades'}
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
      <h1>Hello, ''' + user['Please enter your god name'] + '''</h1>
  </body>
</html>
'''