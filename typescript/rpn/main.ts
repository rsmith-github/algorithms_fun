class RPN_Calculator {
  // no need for constructor.

  // "1 2 +" or 1 3 * 2 + are both valid.
  calculate(postOrderString: string): number {
    // split the input to store in the loop through and evaluate via the stack
    let split: string[] = postOrderString.split(/\s+/);

    // filter out any empty strings that may have been produced by the split method
    split = split.filter((string) => string != "");

    // initialize an empty stack to store numbers
    let stack: number[] = [];

    // loop through each item in the split array
    for (let i: number = 0; i < split.length; i++) {
      // if the item is a number, push it onto the stack
      if (!isNaN(parseInt(split[i]))) {
        stack.push(Number(split[i]));
      }
      // otherwise, the item is an operator, so pop two numbers off the stack and apply the operator
      else {
        let last_in: number | undefined = stack.pop();
        let second_last_in: number | undefined = stack.pop();
        switch (split[i]) {
          case "+":
            // add the two operands and push the result onto the stack
            if (last_in !== undefined && second_last_in !== undefined) {
              let operands: [number, number] = [last_in, second_last_in];
              stack.push(operands[1] + operands[0]);
            }
            break;
          case "-":
            // subtract the two operands and push the result onto the stack
            if (last_in !== undefined && second_last_in !== undefined) {
              let operands: [number, number] = [last_in, second_last_in];
              stack.push(operands[1] - operands[0]);
            }
            break;
          case "*":
            // multiply the two operands and push the result onto the stack
            if (last_in !== undefined && second_last_in !== undefined) {
              let operands: [number, number] = [last_in, second_last_in];
              stack.push(operands[1] * operands[0]);
            }
            break;
          case "/":
            // divide the two operands and push the result onto the stack
            if (last_in !== undefined && second_last_in !== undefined) {
              let operands: [number, number] = [last_in, second_last_in];
              stack.push(operands[1] / operands[0]);
            }
            break;
          case "%":
            // calculate the modulus of the two operands and push the result onto the stack
            if (last_in !== undefined && second_last_in !== undefined) {
              let operands: [number, number] = [last_in, second_last_in];
              stack.push(operands[1] % operands[0]);
            }
            break;
        }
      }
    }
    // the final result is the only item left on the stack, so return it
    return stack[0];
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
result = calculator.calculate("324   +    1 - 23 ");
console.log(result);
