function solution(hp) {
    var a = parseInt(hp/5);
    var b = parseInt((hp-5*a)/3);
    var c = hp -5*a-3*b;

    return a+b+c;
}