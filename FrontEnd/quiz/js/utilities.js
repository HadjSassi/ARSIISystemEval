// -----------------------
// Build the quiz
// -----------------------

function buildQuiz() {
    // we'll need a place to store the HTML output
    const output = [];

    // for each question...
    // we’re using an arrow function to perform our operations on each question. Because this is in a forEach loop, we get the current value, the index, and the array itself as parameters. We only need the current value and the index, which for our purposes, we’ll name currentQuestion and questionNumber respectively.
    myQuestions.forEach((currentQuestion, questionNumber) => {
        // we'll want to store the list of answer choices
        const answers = [];

        // and for each available answer...
        let abc;
        for (abc in currentQuestion.answers) {
            answers.push(
                `<input id="question${questionNumber}${abc}" type="radio" name="question${questionNumber}" class="with-font" value="${abc}">
          <label for="question${questionNumber}${abc}">${currentQuestion.answers[abc]}</label>`
            );
        }

        // add this question and its answers to the output
        output.push(
            `<div class="slide">
            <div id="bg">
              ${currentQuestion.background}
            </div>

            <div id="title" class="wow slideInDown">
              <h2>${currentQuestion.title}</h2>
            </div>

            <div class="question wow fadeIn" data-wow-delay="1s" data-wow-duration="2s">
              <p>${currentQuestion.question}</p>
            </div>

            <div class="answers wow fadeIn" data-wow-delay="2s" data-wow-duration="2s">
              <p>${answers.join("")}</p>
            </div>
         </div>`
        );

    });

    // finally combine our output list into one string of HTML and put it on the page
    quizContainer.innerHTML = output.join("");


};

// -----------------------
// Show Answers
// -----------------------


function showAnswer() {

    const answerTextContainers = quizContainer.querySelectorAll(".answers");

    const answersArray = [];

    // for each question...
    myQuestions.forEach((currentQuestion, questionNumber) => {


        const answerTextContainer = answerTextContainers[questionNumber];

        const selector2 = `input[name=question${questionNumber}]:checked`;

        const userAnswer2 = (answerTextContainer.querySelector(selector2) || {}).value;

        if (userAnswer2 == currentQuestion.correctAnswer) {

            answersArray.push(
                `<div class="slide">
            <div class="answerText wow slideInRight">
              <p>${currentQuestion.correctAnswerText}</p>
            </div>
          </div>`
            );

        } else {

            answersArray.push(
                `<div class="slide">
            <div class="answerText wow slideInRight">
              <p>${currentQuestion.falseAnswerText}</p>
            </div>
          </div>`
            );

        }


    });

    // finally combine our results list into one string of HTML and put it on the page
    resultsTextContainer.innerHTML = answersArray.join("");

    // activate slide
    const answerSlides = resultsTextContainer.querySelectorAll(".slide");
    answerSlides[nSlide].classList.add("active-slide");
    nSlide = nSlide + 1;

    // Show Next Button
    nextButton.classList.remove("displaynone");
    // Disable Answers and Button
    confirmButton.classList.add("disabled");
    $('.answers').addClass('disabled');

    // Show Submit Button on last slide
    // slide Index: 0,1,2,3,4 and Slide length: 5 slides
    if (currentSlide === slides.length - 1) {
        submitButton.style.display = "inline-block";
    }

};


// -----------------------
// Show Results
// -----------------------

function showResults() {
    // gather answer containers from our quiz
    const answerContainers = quizContainer.querySelectorAll(".answers");

    // keep track of user's answers
    let numCorrect = 0;

    // for each question...
    myQuestions.forEach((currentQuestion, questionNumber) => {
        // find selected answer
        // First, we’re making sure we’re looking inside the answer container for the current question.
        const answerContainer = answerContainers[questionNumber];
        // In the next line, we’re defining a CSS selector that will let us find which radio button is checked.
        const selector = `input[name=question${questionNumber}]:checked`;
        // Then we’re using JavaScript’s querySelector to search for our CSS selector in the previously defined answerContainer.
        // this means that we’ll find which answer’s radio button is checked. Finally, we can get the value of that answer by using .value.
        // But what if the user left an answer blank? Then using .value would cause an error because you can’t get the value of something that’s not there.
        // To solve this, we’ve added ||, which means “or” and {} which is an empty object.
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
        // if answer is correct
        if (userAnswer === currentQuestion.correctAnswer) {
            // add to the number of correct answers
            numCorrect++;
        }
    });

    // create dynamic quiz length
    const quizLength = Number(`${myQuestions.length}`);
    // calculate the half of the length
    const quizHalf = Number(`${myQuestions.length}`) / 2;

    // show number of correct answers out of total
    if (numCorrect === quizLength) {
        resultsContainer.innerHTML = `<div class="wow slideInDown"><h2>Congratulations!</h2></div><div class="wow fadeIn" data-wow-delay="1s" data-wow-duration="2s"><p>Very good, you seem to be a pro!</p><p>You answered ${numCorrect} out of ${myQuestions.length} questions correct.</p><a href="http://geobon.org"><button class="btn btn-default">My Dashboard</button></a></div>`;
    } else if (numCorrect >= quizHalf && numCorrect < quizLength) {
        resultsContainer.innerHTML = `<div class="wow slideInDown"><h2>Not bad...</h2></div><div class="wow fadeIn" data-wow-delay="1s" data-wow-duration="2s"><p>but not enough to be a winner.</p><p>You answered just ${numCorrect} out of ${myQuestions.length} questions correct.</p><a href="./index.html"><button id="playAgain" class="btn btn-default">Play again</button></a></div>`;
    } else {
        resultsContainer.innerHTML = `<div class="wow slideInDown"><h2>Very bad...</h2></div><div class="wow fadeIn" data-wow-delay="1s" data-wow-duration="2s"><p>You need to practice! All employees need to be familiar with the iDiv Health & Security rules.</p><p>You answered just ${numCorrect} out of ${myQuestions.length} questions correct.</p><a href="./index.html"><button id="playAgain" class="btn btn-default">Play again</button></a></div>`;
    }

    // switch off Title, Question and Answers
    $('#title h2').css('display', 'none');
    $('.question').css('display', 'none');
    $('.answers').css('display', 'none');
    submitButton.classList.add("displaynone");
    nextButton.classList.add("displaynone");
    confirmButton.classList.add("displaynone");
    resultsTextContainer.innerHTML = '';

};


// -----------------------
// Show Slides
// -----------------------


function showSlide(n) {
    slides[currentSlide].classList.remove("active-slide");
    slides[n].classList.add("active-slide");
    currentSlide = n;

    // show confirmButton by default
    confirmButton.style.display = "inline-block";
    // and switch off other Buttons
    submitButton.style.display = "none";
    nextButton.classList.add("displaynone");

};

// -----------------------
// Show Next Slide
// -----------------------

function showNextSlide() {

    showSlide(currentSlide + 1);

    resultsTextContainer.innerHTML = '';

    // show Answers Options and confirmButton again
    confirmButton.classList.remove("disabled");
    $('.answers').removeClass('disabled');

};

// Export the function for use in other files
export { buildQuiz };
