// Statistics to Doubles
// Implement a ‘die’ that randomly returns an
// integer between 1 and 6 inclusive. Roll a pair of
// these dice, tracking the statistics until doubles
// are rolled. Display the number of rolls, min, max,
// and average.

function randomRoll() {
    return Math.floor(Math.random() * (6 - 1) + 1);
}

function stats() {
    var isDouble = false;
    var numRolls = sum = 0;
    var min = 6;
    var max = 1;

    while(!isDouble) {
        var roll1 = randomRoll();
        var roll2 = randomRoll();

        numRolls++;
        if(roll1 < min) {
            min = roll1;
        }
        if(roll1 > max) {
            max = roll1;
        }
        if(roll2 < min) {
            min = roll2;
        }
        if(roll2 > max) {
            max = roll2;
        }
        sum += roll1 + roll2;

        if (roll1 == roll2) {
            isDouble = true;
        }
    }

    var avg = sum /(numRolls * 2);

    console.log(`Number of rolls: ${numRolls}
        \nMinimum: ${min}
        \nMaximum: ${max}
        \nAverage: ${avg}`)
}

stats();