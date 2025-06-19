const lcsWithDP = require('../services/dpService')


exports.process = (req, res) => {
    let { dataOne, dataTwo } = req.body;

    dataOne = Array.isArray(dataOne) ? dataOne : [dataOne];
    dataTwo = Array.isArray(dataTwo) ? dataTwo : [dataTwo];

    if (!dataOne || !dataTwo || dataOne.length !== dataTwo.length) {
        return res.status(400).send("Dados de entrada inválidos.");
    }
    
    if (dataOne.length > 10) {
         return res.status(400).send("O número máximo de pares é 10.");
    }

    const results = [];

    for (let i = 0; i < dataOne.length; i++) {
        const d1 = dataOne[i].trim();
        const d2 = dataTwo[i].trim();

        if (d1.length > 80 || d1.length < 1 || d2.length > 80 || d2.length < 1) {
            return res.status(400).send(`O Par #${i+1} contém strings com comprimento inválido.`);
        }
        
        const lcsResult = lcsWithDP(d1, d2);

        results.push({
            dataOne: d1,
            dataTwo: d2,
            ...lcsResult
        });
    }

    res.render('dpView', { results: results });
};