const { dividir } = require("./calculadora.js");

describe('Teste de Calculadora', () => {
    test('deve dividir 2 / 2 e retornar 1', () => {
        const num1 = 2;
        const num2 = 2;
        const resultadoEsperado = 1;

        const resultado = dividir(num1, num2);
        expect(resultado).toBe(resultadoEsperado);
    });
});