const start = document.getElementById("startBtn");
const stopsec = document.getElementById("stopBtn");
const reset = document.getElementById("resetBtn");
const timeBox = document.getElementById("timeBox");
const second = document.getElementById("sec");
const milisecond = document.getElementById("milisec");

const recordBox = document.getElementById("recordBox");

let sec = 0;
let milisec = 0;
let count = 0;
let SEC = 0;
let MILI = 0;

function resetFunc() {
  second.innerText = "00";
  milisecond.innerText = "00";
  sec = 0;
  milisec = 0;
}

function startTime() {
  SEC = setInterval(() => {
    sec += 1;
    if (sec < 10) {
      second.innerText = "0" + sec;
    } else {
      second.innerText = sec;
    }
    console.log(sec);
  }, 1000);

  // stop을 클릭할 때마다 시간이 밀리는 현상이 생기는데 이유를 모르겠습니다ㅠㅠ
  MILI = setInterval(() => {
    milisec += 1;
    milisecond.innerText = milisec - sec * 100;
  }, 10);
}

function stopTime() {
  clearInterval(SEC);
  clearInterval(MILI);
}

function recordTime() {
  count += 1;

  //class가 records인 div 태그 생성
  const records = document.createElement("div");
  records.classList.add("records");

  //class가 fa-regular fa-circle인 i 태그 생성 -> 원형 아이콘 유지
  const circleIcon = document.createElement("i");
  circleIcon.classList.add("fa-regular");
  circleIcon.classList.add("fa-circle");

  //id가 recordTime인 div태그 생성
  const recordTime = document.createElement("div");
  recordTime.setAttribute("ID", "recordTime");

  //id가 recordSec, recordMili인 span태그 생성
  const recordSec = document.createElement("span");
  recordSec.setAttribute("ID", "recordSec");
  const recordMili = document.createElement("span");
  recordMili.setAttribute("ID", "recordMili");

  //id가 cnt인 div태그 생성
  const cnt = document.createElement("div");
  cnt.setAttribute("ID", "cnt");

  //recordSec, recordMili를 recordTime 자식으로 추가 -> 기록되는 초
  recordTime.appendChild(recordSec);
  recordTime.appendChild(recordMili);

  //circleIcon, recordTime, cnt를 records 자식으로 추가
  records.appendChild(circleIcon);
  records.appendChild(recordTime);
  records.appendChild(cnt);

  //recordBox에 records를 자식으로 추가 -> stop 클릭시 기록이 아래로 생김
  recordBox.appendChild(records);

  if (sec < 10) {
    recordSec.innerText = "0" + sec;
  } else {
    recordSec.innerText = sec;
  }

  if (milisec - sec * 100 < 10) {
    recordMili.innerText = "0" + milisec - sec * 100;
  } else {
    recordMili.innerText = milisec - sec * 100;
  }

  cnt.innerText = count;

  records.addEventListener("click", () => {
    records.classList.toggle("checked");
    const recordList = document.getElementsByClassName("records");
    for (let i = 0; i < recordList.length; i++) {
      const checkIcon = document.getElementsByClassName("fa-regular")[i + 1];
      if (recordList[i].classList.contains("checked")) {
        checkIcon.classList.remove("fa-circle");
        checkIcon.classList.add("fa-circle-check");
      }
    }
  });

  const trash = document.getElementsByClassName("fa-trash")[0];

  trash.addEventListener("click", () => {
    const recordList = document.getElementsByClassName("records");
    for (let i = 0; i < recordList.length; i++) {
      if (recordList[i].classList.contains("checked")) {
        recordList[i].remove();
      }
    }
  });
}

function keepItChecked() {}

start.addEventListener("click", startTime);
reset.addEventListener("click", resetFunc);
stopsec.addEventListener("click", stopTime);
stopsec.addEventListener("click", recordTime);
