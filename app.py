import os
import sys
from flask import Flask, jsonify, request, render_template_string

# Garante que o diretório raiz esteja no path para importar src.python.calculadora
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.python.calculadora import soma, subtracao, multiplicacao, divisao

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora FATEC - Docker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            width: 360px;
            text-align: center;
        }
        h2 { color: #b20000; margin-bottom: 5px; }
        p { color: #666; font-size: 14px; margin-bottom: 20px; }
        .form-group { margin-bottom: 15px; text-align: left; }
        label { display: block; font-weight: bold; font-size: 13px; margin-bottom: 5px; }
        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 14px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #b20000;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover { background: #8c0000; }
        .resultado {
            margin-top: 20px;
            padding: 12px;
            background: #eef2f7;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }
        .info {
            margin-top: 15px;
            font-size: 12px;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Calculadora FATEC</h2>
        <p>Projeto conteinerizado com Docker na porta 5000</p>
        <div class="form-group">
            <label for="num1">Primeiro Número:</label>
            <input type="number" id="num1" step="any" value="10">
        </div>
        <div class="form-group">
            <label for="operacao">Operação:</label>
            <select id="operacao">
                <option value="soma">Soma (+)</option>
                <option value="subtracao">Subtração (-)</option>
                <option value="multiplicacao">Multiplicação (*)</option>
                <option value="divisao">Divisão (/)</option>
            </select>
        </div>
        <div class="form-group">
            <label for="num2">Segundo Número:</label>
            <input type="number" id="num2" step="any" value="2">
        </div>
        <button onclick="calcular()">Calcular</button>
        <div class="resultado" id="res">Resultado: 12</div>
        <div class="info">API: /soma, /subtracao, /multiplicacao, /divisao?a=&b=</div>
    </div>

    <script>
        async function calcular() {
            const a = document.getElementById('num1').value;
            const b = document.getElementById('num2').value;
            const op = document.getElementById('operacao').value;
            const resDiv = document.getElementById('res');
            
            try {
                const response = await fetch(`/${op}?a=${a}&b=${b}`);
                const data = await response.json();
                if (data.error) {
                    resDiv.innerText = 'Erro: ' + data.error;
                    resDiv.style.color = 'red';
                } else {
                    resDiv.innerText = `Resultado: ${data.resultado}`;
                    resDiv.style.color = '#333';
                }
            } catch (e) {
                resDiv.innerText = 'Erro ao conectar ao servidor';
                resDiv.style.color = 'red';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/soma')
def route_soma():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'operacao': 'soma', 'a': a, 'b': b, 'resultado': soma(a, b)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/subtracao')
def route_subtracao():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'operacao': 'subtracao', 'a': a, 'b': b, 'resultado': subtracao(a, b)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/multiplicacao')
def route_multiplicacao():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'operacao': 'multiplicacao', 'a': a, 'b': b, 'resultado': multiplicacao(a, b)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/divisao')
def route_divisao():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        if b == 0:
            return jsonify({'error': 'Divisão por zero não permitida'}), 400
        return jsonify({'operacao': 'divisao', 'a': a, 'b': b, 'resultado': divisao(a, b)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
