const bnt = document.querySelector(".submit-button");
let cnt = 0;
const img = document.querySelector("img");
let outCount = 0;
const result = document.querySelector(".result-display");
const myAnswer = document.querySelector(".left");
const clue = document.querySelector(".right");

let answerNumber = [];
for (i = 0; i < 3; i++) {
  let num = Math.floor(Math.random() * 9 + 1);
  if (answerNumber.indexOf(num) === -1) {
    answerNumber.push(num);
  } else {
    i--;
  }
}
console.log(answerNumber);

function attemptChecker() {
  cnt += 1;
  console.log(cnt);
  if (cnt === 9) {
    img.src = "./fail.png";
  }
}

function resetNum() {
  let inputNumber1 = document.querySelector("#number1");
  inputNumber1.value = null;
  let inputNumber2 = document.querySelector("#number2");
  inputNumber2.value = null;
  let inputNumber3 = document.querySelector("#number3");
  inputNumber3.value = null;
}

function check_numbers() {
  let num1 = document.getElementById("number1").value;
  let num2 = document.getElementById("number2").value;
  let num3 = document.getElementById("number3").value;
  let tryNumber = [];
  tryNumber[0] = num1;
  tryNumber[1] = num2;
  tryNumber[2] = num3;
  console.log(tryNumber);
  let strikeCount = 0;
  let ballCount = 0;

  for (i = 0; i < 3; i++) {
    if (num1 == answerNumber[i]) {
      if (i == 0) {
        strikeCount += 1;
      } else {
        ballCount += 1;
      }
    }

    if (num2 == answerNumber[i]) {
      if (i == 1) {
        strikeCount += 1;
      } else {
        ballCount += 1;
      }
    }

    if (num3 == answerNumber[i]) {
      if (i == 2) {
        strikeCount += 1;
      } else {
        ballCount += 1;
      }
    }
  }

  if (strikeCount == 0 && ballCount == 0) {
    outCount += 1;
  }

  if (outCount > 0) {
    strikeAndBall = result.children[0];
    result.appendChild(strikeAndBall);
  }

  myAnswer.innerHTML = tryNumber;
  clue.childNodes[0].nodeValue = strikeCount;
  clue.childNodes[2].nodeValue = ballCount;

  if (strikeCount == 3) {
    img.src = "./success.png";
  }

  console.log(strikeCount, ballCount, outCount);
  console.log(result);
}

bnt.addEventListener("click", attemptChecker);
bnt.addEventListener("click", resetNum);
