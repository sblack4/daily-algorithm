/**
 * gets user input
 * tests to see if palindrome
 * returns result to console
 */
const readline = require('readline');


function get_input() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise((resolve, reject) => {
        rl.question("Test a palindrome: \n ", (input_string) => {

            resolve(input_string);

            rl.close();
        });
    });
}

function is_palindrome(input_string) {
    let half_input_length = Math.round(input_string.length / 2);
    let input_array = input_string.split("");

    for (let i = 0; i < half_input_length; i++) {
        // console.log(input_array[input_string.length - i - 1]);
        if (input_array[i] != input_array[input_string.length - i - 1]) {
            return false;
        }
    }
    return true;
}

function main() {
    get_input()
        .then((input_string) => {
            palindrome_bool = is_palindrome(input_string);
            console.log(input_string + " is a palindrome " + palindrome_bool);
        })
}

if (require.main === module) {
    main();
}