class RPN_Calculator {

    // no need for constructor.

    // "1 2 +" or 1 3 * 2 + are both valid.
    calculate(postOrderString: string): number {

        // split the input to store in the loop through and evaluate via the stack
        let split: string[] = postOrderString.split(/\s+/);

        split = split.filter(string => string != "");

        let stack: number[] = [];

        for (let i: number = 0; i < split.length; i++) {
            
            if (!isNaN(parseInt(split[i]))) {
                stack.push(Number(split[i]));
            } else {
                let last_in: number | undefined = stack.pop();
                let second_last_in: number | undefined = stack.pop();
                switch (split[i]) {
                    case "+":
                        if (last_in !== undefined && second_last_in !== undefined) {
                            let operands: [number, number] = [last_in, second_last_in];
                            stack.push(operands[1] + operands[0])
                        }
                        break
                    case "-":
                        if (last_in !== undefined && second_last_in !== undefined) {
                            let operands: [number, number] = [last_in, second_last_in];
                            stack.push(operands[1] - operands[0])
                        }
                        break
                    case "*":
                        if (last_in !== undefined && second_last_in !== undefined) {
                            let operands: [number, number] = [last_in, second_last_in];
                            stack.push(operands[1] * operands[0])
                        }
                        break
                    case "/":
                        if (last_in !== undefined && second_last_in !== undefined) {
                            let operands: [number, number] = [last_in, second_last_in];
                            stack.push(operands[1] / operands[0])
                        }
                        break
                    case "%":
                        if (last_in !== undefined && second_last_in !== undefined) {
                            let operands: [number, number] = [last_in, second_last_in];
                            stack.push(operands[1] % operands[0])
                        }
                        break
                }       
            
            }

        }
        return stack[0]

    }
    
}


let calculator: RPN_Calculator = new RPN_Calculator();
let result = calculator.calculate("1 2 3 4  + + +");
console.log(result);
result = calculator.calculate("11 22 +");
console.log(result);
result = calculator.calculate("11016 153 /");
console.log(result);
result = calculator.calculate("15 76 *");
console.log(result);
result = calculator.calculate("23491234 102030932 -");
console.log(result);
result = calculator.calculate("1 2 * 3 * 4 +");
console.log(result);
result = calculator.calculate("3 1 2 * * 4 %");
console.log(result);
result = calculator.calculate("5 10 2 / - 50 *");
console.log(result);
result = calculator.calculate("299   255 %");
console.log(result);
result = calculator.calculate("     1      3 * 2 -");
console.log(result);
