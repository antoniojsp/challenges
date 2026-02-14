
// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/



function evalRPN(tokens: string[]): number {
    const S:number[] = [];
    for(const token of tokens){
        if(!isNaN(Number(token))){
            S.push(parseInt(token));
        }else{
            const b = S.pop()!;
            const a = S.pop();
            let result = 0;
            switch (token){
                case "*":
                    result = a*b;
                    break;
                case "+":
                    result = a+b;
                    break;
                case "-":
                    result = a-b;
                    break;
                case "/":
                    result = Math.trunc(a/b);
                    break;
            }
            S.push(result)
        }
    }
    return S[0];
};
