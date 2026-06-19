from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Sky Blue Calculator</title>
<style>
body{
    background:#f0f8ff;
    font-family:Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

.calculator{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 0 15px gray;
}

#display{
    width:100%;
    height:60px;
    font-size:28px;
    text-align:right;
    margin-bottom:10px;
}

.buttons{
    display:grid;
    grid-template-columns:repeat(4,70px);
    gap:10px;
}

button{
    height:60px;
    font-size:24px;
    border:none;
    border-radius:10px;
    cursor:pointer;
}

.digit{
    color:skyblue;
    font-weight:bold;
}

.operator{
    background:orange;
    color:white;
}

.equal{
    background:green;
    color:white;
}

.clear{
    background:red;
    color:white;
}
</style>
</head>
<body>

<div class="calculator">

<input type="text" id="display" readonly>

<div class="buttons">
<button class="digit" onclick="add('7')">7</button>
<button class="digit" onclick="add('8')">8</button>
<button class="digit" onclick="add('9')">9</button>
<button class="operator" onclick="add('/')">÷</button>

<button class="digit" onclick="add('4')">4</button>
<button class="digit" onclick="add('5')">5</button>
<button class="digit" onclick="add('6')">6</button>
<button class="operator" onclick="add('*')">×</button>

<button class="digit" onclick="add('1')">1</button>
<button class="digit" onclick="add('2')">2</button>
<button class="digit" onclick="add('3')">3</button>
<button class="operator" onclick="add('-')">−</button>

<button class="digit" onclick="add('0')">0</button>
<button class="digit" onclick="add('.')">.</button>
<button class="equal" onclick="calculate()">=</button>
<button class="operator" onclick="add('+')">+</button>

<button class="clear" onclick="clearDisplay()" style="grid-column: span 4;">
Clear
</button>
</div>

</div>

<script>
function add(value){
    document.getElementById("display").value += value;
}

function calculate(){
    try{
        document.getElementById("display").value =
        eval(document.getElementById("display").value);
    }
    catch{
        document.getElementById("display").value = "Error";
    }
}

function clearDisplay(){
    document.getElementById("display").value = "";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)