const { somar } = require("./calculadora.js");

describe('Teste de Calculadora', () => {
    test('deve somar 1 + 2 e retornar 3', () => {
        const num1 = 1;
        const num2 = 2;
        const resultadoEsperado = 3;

        const resultado = somar(num1, num2);
        expect(resultado).toBe(resultadoEsperado);
    });
});