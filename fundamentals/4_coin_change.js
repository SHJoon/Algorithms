// Generate Coin Change
// Implement generateCoinChange(cents) that accepts a parameter for the number of cents,
// and computes how to represent that amount with the smallest number of coins.
// Console.log the result.

function generateCoinChange(cents) {
    var quarters = Math.floor(cents / 25);
    cents = cents - (quarters * 25); 

    var dimes = Math.floor(cents / 10);
    cents = cents - (dimes * 10); 

    var nickels = Math.floor(cents / 5);

    var pennies = cents - (nickels * 5);

    var numCoins = quarters + dimes + nickels + pennies;

    console.log("Number of coins: " + String(numCoins));
}

generateCoinChange(99);