/*
import { buildQuiz } from './utilities.js';

const myQuestions = [];

function getUrlParameter(name) {
  name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
  var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
  var results = regex.exec(location.search);
  return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

async function fetchQuestions() {
  return new Promise((resolve, reject) => {
    var idvar = getUrlParameter('id');
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/subject?id=" + idvar, true);
    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        reject("GET request failed with status: " + xhr.status);
      }
    };
    xhr.onerror = function () {
      reject("GET request failed!");
    };
    xhr.send();
  });
}

async function loadQuestions() {
  try {
    const questionsData = await fetchQuestions();
    questionsData.forEach((questionData, index) => {
      myQuestions.push({
        title: `Question ${index + 1}`,
        question: questionData.question,
        background: `<img src='./img/${index + 1}.jpg'>`,
        answers: questionData.answers,
        correctAnswer: questionData.correctAnswer,
        correctAnswerText: questionData.correctAnswerText,
        falseAnswerText: questionData.falseAnswerText
      });
    });
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", async function () {
  await loadQuestions();
  buildQuiz();
  const confirmButton = document.getElementById("confirm");

  const nextButton = document.getElementById("next");

  const submitButton = document.getElementById("submit");

  const slides = document.querySelectorAll(".slide");

  const answers = document.querySelectorAll(".answers");

  // -----------------------
  // Show Starting Slide (Index)
  // -----------------------

  let currentSlide = 0;
  let nSlide = 0;
  showSlide(0);

  // -----------------------
  // Click Events
  // -----------------------

  confirmButton.addEventListener("click", showAnswer);

  nextButton.addEventListener("click", showNextSlide);

  submitButton.addEventListener("click", showResults);

  console.log(myQuestions);
  // Once questions are loaded, proceed with other initialization and display logic
});
*/
