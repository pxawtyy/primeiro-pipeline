const { multiplicar } = require("./calculadora.js");

describe('Teste de Calculadora', () => {
    test('deve multiplicar 2 * 2 e retornar 4', () => {
        const num1 = 2;
        const num2 = 2;
        const resultadoEsperado = 4;

        const resultado = multiplicar(num1, num2);
        expect(resultado).toBe(resultadoEsperado);
    });
});