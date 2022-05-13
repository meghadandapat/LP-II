


let btn = document.getElementById("btn")

function multiply(mat1, mat2, res) {
    let i, j, k;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            res[i][j] = 0;
            for (k = 0; k < 3; k++)
                res[i][j] += mat1[i][k] * mat2[k][j];
        }
    }
}

btn.addEventListener("click", () => {
    let input1 = document.getElementById("input1").value
    let input2 = document.getElementById("input2").value
    let table1 = document.getElementById("table1")
    let table2 = document.getElementById("table2")
    let res = document.getElementById("res")
    let x = input1.split("#").map(Number)
    let y = input2.split("#").map(Number)
    let mat1 = []
    let mat2 = []
    let r = "";
    let z = ""
    let z1 = ""
    let r1 = ""
    let row1 = x[0], column1 = x[1], num1 = x[2]
    let row2 = y[0], column2 = y[1], num2 = y[2]

    for (let i = 0; i < row1; i++) {
        let lst = []
        num = num1 * (i + 1)
        r = "<tr>";
        for (let j = 0; j < column1; j++) {

            r += `<td> ${num} </td>`
            lst.push(num)
            num += (i + 1);
        }
        mat1.push(lst)
        r += "</tr>"
        z += r
    }
    table1.innerHTML = z;


    for (let i = 0; i < row2; i++) {
        let lst = []
        num = num2 * (i + 1)
        r1 = "<tr>";
        for (let j = 0; j < column2; j++) {

            r1 += `<td> ${num} </td>`
            lst.push(num)
            num += (i + 1);
        }
        mat2.push(lst)
        r1 += "</tr>"
        z1 += r1
    }
    table2.innerHTML = z1;

    let result = new Array(3);
    for (let k = 0; k < 3; k++)
        result[k] = new Array(3);

    multiply(mat1, mat2, result)
    // console.log(result)

    z = ""
    r = ""
    if (num1 == num2) {
        z = ""
        r = ""
        for (let i = 0; i < row1; i++) {
            let lst = []
            num = num1 * (i + 1)
            r = "<tr>";
            for (let j = 0; j < column1; j++) {

                r += `<td> ${num} </td>`
                lst.push(num)
                num += (i + 1);
            }
            mat1.push(lst)
            r += "</tr>"
            z += r
        }
        res.innerHTML = z;
    }
    else {
        z = ""
        r = ""
        for (let i = 0; i < 3; i++) {
            r = "<tr>";
            for (let j = 0; j < 3; j++) {
                r += `<td> ${result[i][j]} </td>`
            }
            r += "</tr>"
            z += r

        }
        res.innerHTML = z;
    }

})




