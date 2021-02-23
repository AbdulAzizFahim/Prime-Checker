from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/', defaults={'result': "Unavailable!"})
@app.route('/<result>')
def mainpage(result):
    return render_template("index.html", result = result)


def checker(input):
    x = 2
    data = int(input)
    flag = True
    while(x*x<=data):
         if(data%x == 0):
            flag = False
         else:
            x+=1
         if(flag == False):
            break
    if(data == 1):
        flag = False
    return flag     


@app.route('/submit',methods = ['GET'])
def submit():
   if request.method == 'GET':
    left = request.args['number1'];
    right = request.args['number2'];
    L = int(left)
    R= int (right)
    cnt = 0;
    flag = True
    if(L>R): 
        ans = "INVALID RANGE"
        flag = False
    else:
        while(L<=R):
            if(checker(L) == True):
                cnt+=1
                L+=1
            else:
                L+=1
            
    if(flag == True):  
        return redirect(url_for('mainpage',result = "{}".format(cnt)))
    else:
        return redirect(url_for('mainpage',result = "{}".format(ans)))
   else:
        return redirect(url_for('mainpage',result = "Something went wrong!"))

if __name__ == '__main__':
    app.run()
