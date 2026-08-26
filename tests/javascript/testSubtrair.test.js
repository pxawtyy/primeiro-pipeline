const { subtrair } = require("./calculadora.js");

describe('Teste de Calculadora', () => {
    test('deve subtrair 2 - 1 e retornar 1', () => {
        const num1 = 2;
        const num2 = 1;
        const resultadoEsperado = 1;

        const resultado = subtrair(num1, num2);
        expect(resultado).toBe(resultadoEsperado);
    });
});